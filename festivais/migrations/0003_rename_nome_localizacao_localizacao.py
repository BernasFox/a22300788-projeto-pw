# Generated by Django 4.0.6 on 2024-04-24 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivais', '0002_alter_festival_localizacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localizacao',
            old_name='nome',
            new_name='localizacao',
        ),
    ]
