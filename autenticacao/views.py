from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('meusite:index'))
    return render(request, 'autenticacao/login.html')

def logout_user(request):
    logout(request)
    return redirect(reverse('meusite:index'))



def login_user_withredirect(request, site):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse(site + ':index'))
    return render(request, 'autenticacao/login.html')

def logout_user_withredirect(request, site):
    logout(request)
    return redirect(reverse(site + ':index'))


def password_reset(request):
    # Sua lógica de recuperação de senha aqui
    return render(request, 'curso/password_reset.html')

def password_reset_done(request):
    # Sua lógica de recuperação de senha feita aqui
    return render(request, 'curso/password_reset_done.html')

def password_reset_confirm(request, uidb64, token):
    # Sua lógica de confirmação de recuperação de senha aqui
    return render(request, 'curso/password_reset_confirm.html')

def password_reset_complete(request):
    # Sua lógica de recuperação de senha completa aqui
    return render(request, 'curso/password_reset_complete.html')







