from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='bandas', blank=True)
    album = models.ManyToManyField('Album', blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    nome = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='albuns', blank=True)
    musicas = models.ManyToManyField('Musica', blank=True)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    foto = models.ImageField(upload_to='musicas', blank=True)
    biografia = models.CharField(max_length=1000, null = True, blank = True)

    def __str__(self):
        return self.titulo
