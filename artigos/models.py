from django.db import models

# Create your models here.
class Autor(models.Model):
    user = models.CharField(max_length = 100)
    bio = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='autores', blank=True)

    def __str__(self):
        return f"{self.user}"

class Artigo(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) # Permite selecionar apenas a partir dos Autores
    titulo = models.CharField(max_length = 200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem_destaque = models.ImageField(upload_to='artigos', blank=True)

    def __str__(self):
        return f"{self.titulo}"

class Comentario(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário por User: {self.autor.user} em Artigo: {self.artigo.titulo}'
