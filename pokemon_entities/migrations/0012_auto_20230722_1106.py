# Generated by Django 3.1.14 on 2023-07-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20230722_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.FloatField(blank=True, verbose_name='Уровень'),
        ),
    ]