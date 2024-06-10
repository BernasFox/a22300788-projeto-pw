from django.db import models
from django.urls import reverse

class Tipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Trabalho(models.Model):
    nome = models.CharField(max_length=100)
    url = models.CharField(max_length=100)  # Change CharField to URLField
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse(self.url)
