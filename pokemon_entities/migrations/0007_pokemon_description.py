# Generated by Django 2.2.3 on 2019-11-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20191119_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
