# Generated by Django 4.0.6 on 2024-04-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_permicoes_tipo_permicoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo',
            name='permicoes',
        ),
        migrations.AddField(
            model_name='user',
            name='permicoes',
            field=models.ManyToManyField(to='users.permicao'),
        ),
    ]