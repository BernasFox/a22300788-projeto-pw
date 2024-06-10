from django.shortcuts import render
from .models import *
# Create your views here.


def index_view(request):
    return render(request, "festivais/index.html")

def festival_view(request, id_festival):
    context = {
        'festival': Festival.objects.get(id = id_festival)
    }
    return render(request, "festivais/festivais.html", context)

def festivais_view(request):
    # Localizacao
    context = {
        'localizacoes': Localizacao.objects.all().order_by('localizacao')
    }
    return render(request, "festivais/localizacao.html", context)