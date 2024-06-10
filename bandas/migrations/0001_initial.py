# Generated by Django 4.0.6 on 2024-04-25 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('capa', models.ImageField(blank=True, upload_to='albuns')),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True)),
                ('foto', models.ImageField(blank=True, upload_to='musicas')),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, upload_to='bandas')),
                ('album', models.ManyToManyField(to='bandas.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='musicas',
            field=models.ManyToManyField(to='bandas.musica'),
        ),
    ]
