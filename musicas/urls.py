from django.urls import path
from . import views  # importamos views para poder usar as suas funções
from autenticacao import views as autentic

app_name = 'musicas'

urlpatterns = [
    path('', views.index_view, name='index'),

]