# Generated by Django 4.0.6 on 2024-04-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivais', '0008_remove_festival_imagem_banda_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='imagem',
            field=models.ImageField(default='', upload_to='bandas'),
            preserve_default=False,
        ),
    ]
