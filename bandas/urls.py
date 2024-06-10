from django.urls import path
from . import views  # importamos views para poder usar as suas funções
from autenticacao import views as autentic

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view, name='index'),

    # Mostrar busca
    path('<str:tipo>/<int:nome_data>', views.show_view, name='show'),

    # Mostrar todas
    path('<str:tipo>/', views.show_all_view, name='show_all'),

    # Editar
    path('<str:tipo>/edit/<int:id_data>', views.edit_view, name='edit'),

    path('apagar/<str:tipo>', views.apagar_view, name='apagar'),
    path('apagar/<str:tipo>/<int:id_data>', views.apagar, name='apagar_data'),


    path('inserir/<str:tipo>', views.insert_view, name = 'inserir'),

    path('login/', autentic.login_user, name = 'login'),
    path('logout/', autentic.logout_user, name = 'logout'),
]