from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    tipo = models.ManyToManyField('Tipo')
    permicoes = models.ManyToManyField('Permicao')

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=100)


    def __str__(self):
        return self.nome

class Permicao(models.Model):
    permicao = models.CharField(max_length=100)

    def __str__(self):
        return self.permicao
