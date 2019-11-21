import folium
import json
import branca

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL, popup='Это что за покемон?'):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )

    iframe = branca.element.IFrame(html=popup, width=300, height=200)
    popup = folium.Popup(iframe, max_width=500)

    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
        popup=popup
    ).add_to(folium_map)


def show_all_pokemons(request):

    pokemons_qs = Pokemon.objects.all()


    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    
    for pokemon in pokemons_qs:
        for pokemon_entity in pokemon.poke.all():
            pokemon_popup = f'HP: {pokemon_entity.health} \n Сила: {pokemon_entity.strength}'
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon,
                pokemon.title, request.build_absolute_uri(pokemon.image.url),
                pokemon_popup)


    pokemons_on_page = []
    for pokemon in pokemons_qs:
        if pokemon.image:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'img_url': pokemon.image.url,
                'title_ru': pokemon.title,
            })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    previous_evolution = pokemon.next_pokemon.filter(next_evolution=pokemon.id).first()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon.poke.all():
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon.title, request.build_absolute_uri(pokemon.image.url))

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon,
                                                    'previous_evolution': previous_evolution})
