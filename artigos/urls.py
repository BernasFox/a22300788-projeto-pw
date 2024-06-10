from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'artigos'

urlpatterns = [
    # Mostrar busca
    # path('musicas/<str:nome_musica>', views.musicas_view, name='musicas_url'),

    # Mostrar todas
    path('', views.index_view, name='index'),
    path('artigos/', views.index_view, name='artigos'),
    path('autores/', views.index_view, name='autores'),
]