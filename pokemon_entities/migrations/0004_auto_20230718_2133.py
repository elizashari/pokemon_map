# Generated by Django 3.1.14 on 2023-07-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20230718_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
