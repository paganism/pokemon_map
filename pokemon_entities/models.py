import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(max_length=200, verbose_name='Название англ.')
    title_jp = models.CharField(max_length=200, verbose_name='Название яп.')
    image = models.ImageField(storage=fs, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    next_evolution = models.ForeignKey('Pokemon',
                                        on_delete=models.SET_NULL,
                                        blank=True,
                                        null=True,
                                        related_name='next_pokemon',
                                        verbose_name='В кого эволюционирует')
    previous_evolution = models.ForeignKey('Pokemon',
                                            on_delete=models.SET_NULL,
                                            blank=True,
                                            null=True,
                                            related_name='previous_pokemon',
                                            verbose_name='Из кого эволюционирует')

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='poke', verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Когда появится')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Когда исчезнет')
    level = models.IntegerField(default=100, verbose_name='Уровень')
    health = models.IntegerField(default=100, verbose_name='Здоровье')
    strength = models.IntegerField(default=100, verbose_name='Сила')
    defence = models.IntegerField(default=100, verbose_name='Защита')
    Stamina = models.IntegerField(default=100, verbose_name='Выносливость')
