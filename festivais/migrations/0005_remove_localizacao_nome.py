# Generated by Django 4.0.6 on 2024-04-24 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivais', '0004_localizacao_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localizacao',
            name='nome',
        ),
    ]
