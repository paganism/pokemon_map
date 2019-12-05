# Generated by Django 2.2.3 on 2019-11-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20191120_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonelementtype',
            name='pokemon',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='element_type',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(to='pokemon_entities.PokemonElementType'),
        ),
    ]