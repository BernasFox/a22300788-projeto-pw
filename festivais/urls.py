from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'festivais'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('festivais/', views.festivais_view, name='festivais'),
    path('festival/<int:id_festival>/', views.festival_view, name='festival'),
]