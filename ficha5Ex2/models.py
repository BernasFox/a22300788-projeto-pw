from django.db import models

# Create your models here.

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    ano_criacao = models.IntegerField()
    nacionalidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disco(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()

    def __str__(self):
        return self.titulo

class Musica(models.Model):
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE, related_name='musicas')
    titulo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo
