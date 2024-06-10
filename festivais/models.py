from django.db import models

class Localizacao(models.Model):
    localizacao = models.CharField(max_length=100)
    festivais = models.ManyToManyField('Festival')
    def __str__(self):
        return self.localizacao

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    bandas = models.ManyToManyField('Banda')
    imagem = models.ImageField(upload_to='bandas')

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField()
    def __str__(self):
        return self.nome