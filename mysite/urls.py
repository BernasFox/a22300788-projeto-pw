"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


app_name = 'index'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meusite.urls')),  # novo path
    path('noobsite/', include('noobsite.urls')),  # novo path
    path('pwsite/', include('pwsite.urls')),  # novo path
    path('novaapp/', include('novaapp.urls')),  # novo path
    path('bandas/', include('bandas.urls')),  # novo path
    path('artigos/', include('artigos.urls')),  # novo path
    path('curso/', include('curso.urls')),  # novo path
    path('festivais/', include('festivais.urls')),  # novo path
    path('musicas/', include('musicas.urls')),  # novo path
    path('meteo/', include('meteo.urls')),  # novo path

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]