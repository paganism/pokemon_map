# Generated by Django 2.2.3 on 2019-11-19 08:58

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20191117_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/yoj/devman/pokemon_map/media'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
