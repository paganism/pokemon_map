# Generated by Django 2.2.3 on 2019-11-17 09:51

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/yoj/devman/pokemon_map/media/images'), upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon')),
            ],
        ),
    ]
