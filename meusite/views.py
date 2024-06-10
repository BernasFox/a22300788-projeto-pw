from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from random import randint



def download_template():
    # URL do template do Canva
    canva_url = "https://www.canva.com/design/DAGCaKpqcBA/V9xgU03RIOccfSNa6ybY8Q/view"

    # Solicita o conteúdo do Canva
    response = requests.get(canva_url)

    # Retorna o conteúdo como um arquivo PDF
    return send_file(response.content, mimetype='application/pdf', as_attachment=True, attachment_filename='meu_template.pdf')


def get_frase():
    frases = [
        "Bem-vindo ao meu portfólio! Explore meu trabalho e descubra mais sobre mim.",
        "Olá! Fico feliz em vê-lo aqui. Navegue pelo site e conheça meus projetos.",
        "Seja bem-vindo! Sinta-se à vontade para explorar minhas criações.",
        "Bem-vindo ao meu espaço criativo! Espero que goste do que verá.",
        "Olá e bem-vindo! Aqui você encontrará um pouco sobre minha jornada e meus trabalhos.",
        "Bem-vindo! Agradeço sua visita e espero que se inspire com meus projetos.",
        "Seja bem-vindo ao meu portfólio online! Fique à vontade para explorar e entrar em contato.",
        "Olá! Obrigado por visitar meu site. Explore minhas obras e saiba mais sobre mim.",
        "Bem-vindo! Confira meus trabalhos e projetos recentes aqui.",
        "Seja bem-vindo ao meu cantinho na web! Aproveite para conhecer um pouco mais sobre meu trabalho.",
    ]
    frase = frases[randint(0,len(frases)-1)]
    return frase

def index_view(request):


    context = {'frase': get_frase()}
    return render(request, "meusite/index.html", context)

def aboutme_view(request):
    return render(request, "meusite/aboutme.html")

@login_required
def admin_view(request):
    return render(request, "meusite/admin.html")

def trabalhos_view(request):
    sites = Tipo.objects.get(nome='Pessoal/sites')
    programas = Tipo.objects.get(nome='Pessoal/programas')
    context = {
        'programas': Trabalho.objects.filter(tipo=programas.id).order_by('nome'),
        'sites': Trabalho.objects.filter(tipo=sites.id).order_by('nome')
    }

    return render(request, "meusite/trabalhos.html", context)

def faculdade_view(request):
    sites = Tipo.objects.get(nome='Faculdade/sites')
    programas = Tipo.objects.get(nome='Faculdade/programas')
    context = {
        'programas': Trabalho.objects.filter(tipo=programas.id).order_by('nome'),
        'sites': Trabalho.objects.filter(tipo=sites.id).order_by('nome')
    }
    return render(request, "meusite/faculdade.html", context)



