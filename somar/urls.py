from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'somar'

urlpatterns = [
    # Mostrar busca
    # path('musicas/<str:nome_musica>', views.musicas_view, name='musicas_url'),

    # Mostrar todas
    path('', views.somar, name='index'),
]