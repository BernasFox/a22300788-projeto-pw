# Generated by Django 4.0.6 on 2024-04-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivais', '0009_festival_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='imagem',
            field=models.ImageField(upload_to=''),
        ),
    ]