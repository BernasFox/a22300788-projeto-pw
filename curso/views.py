from django.shortcuts import render, get_object_or_404, redirect
from . import views
from .models import *
from .forms import *
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def index_view(request):
    return listar_cursos(request)

@login_required
def editar_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:listar_disciplinas_curso', curso_id=disciplina.curso.id)
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'curso/editar_disciplina.html', {'form': form})

@login_required
def editar_docente(request, docente_id):
    docente = get_object_or_404(Docente, pk=docente_id)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('curso:listar_docentes')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'curso/editar_docente.html', {'form': form})


def listar_cursos(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'curso/curso.html', context)

def listar_disciplinas_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    disciplinas = Curso.objects.get(id=curso_id).disciplinas.annotate(num_projetos = Count('projetos')).order_by('ano', '-num_projetos')
    context = {
        'curso': curso,
        'disciplinas': disciplinas
    }
    return render(request, 'curso/disciplinas.html', context)

def detalhes_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    context = {
        'projeto': projeto
    }
    return render(request, 'curso/detalhes_projeto.html', context)

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

def listar_docentes(request):
    docentes = Docente.objects.all()
    context = {
        'docentes': docentes
    }
    return render(request, 'curso/docentes.html', context)

def listar_projetos_disciplinas(request):
    projetos = Projeto.objects.all()
    context = {
        'projetos': projetos
    }
    return render(request, 'curso/projeto.html', context)




