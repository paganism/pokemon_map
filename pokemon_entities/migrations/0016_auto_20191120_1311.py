# Generated by Django 2.2.3 on 2019-11-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20191120_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(related_name='element_type', to='pokemon_entities.PokemonElementType'),
        ),
    ]
