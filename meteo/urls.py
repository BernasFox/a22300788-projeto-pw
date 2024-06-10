from django.urls import path, include
from . import views  # importamos views para poder usar as suas funções
from django.contrib.auth import views as auth_views
from autenticacao import views as autentic

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:id>/<int:dia>', views.city_dia_view, name='hoje'),
    path('<int:id>/', views.city_view, name='cidade'),

    path('login/', autentic.login_user, name = 'login'),
    path('logout/', autentic.logout_user, name = 'logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]