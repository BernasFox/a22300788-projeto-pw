from django.contrib import admin

# Register your models here.
from .models import Autor, Artigo, Comentario

admin.site.register(Autor)
admin.site.register(Artigo)
admin.site.register(Comentario)