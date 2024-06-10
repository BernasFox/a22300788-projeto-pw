from django.urls import path, include
from . import views  # importamos views para poder usar as suas funções
from django.contrib.auth import views as auth_views
from autenticacao import views as autentic

app_name = 'meusite'

urlpatterns = [
    path('trabalhos/', views.trabalhos_view, name='trabalhos'),
    path('aboutme/', views.aboutme_view, name='aboutme'),
    path('faculdade/', views.faculdade_view, name='faculdade'),
    path('admin-tools/', views.admin_view, name='admin'),
    path('', views.index_view, name='index'),


    path('login/', autentic.login_user, name = 'login'),
    path('logout/', autentic.logout_user, name = 'logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]