from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('sobre/', views.sobre_view, name='sobre'),
    path('sobremim/', views.sobremim_view, name='sobremim'),
    path('', views.index_view, name='index'),
]
