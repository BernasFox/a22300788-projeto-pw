from django.shortcuts import render
from artigos.models import *

# Create your views here.

# def musicas_view(request, nome_musica):
#     context = {
#         'musica': Musica.objects.get(id= nome_musica),
#     }
#     return render(request, "bandas/musicas.html", context)


def index_view(request):
    context = {
        'data': Autor.objects.all().order_by('user')
    }

    return render(request, "artigos/index.html", context)


# all
# def all_musicas_view(request):
#     context = {
#         'data': Musica.objects.all().order_by('titulo'),
#     }
#     return render(request, "bandas/all_musicas.html", context)

