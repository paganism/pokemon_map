# Generated by Django 2.2.3 on 2019-11-26 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0028_auto_20191126_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to='pokemon_entities.Pokemon', verbose_name='Покемон'),
        ),
    ]
