from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from autenticacao import views as autentic
app_name = 'curso'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('', listar_cursos, name='listar_cursos'),
    path('curso/<int:curso_id>/disciplinas/', listar_disciplinas_curso, name='listar_disciplinas_curso'),
    path('projetos/', listar_projetos_disciplinas, name='listar_projetos_disciplinas'),
    path('projeto/<int:projeto_id>/', detalhes_projeto, name='detalhes_projeto'),
    path('docentes/', listar_docentes, name='listar_docentes'),
    path('disciplina/editar/<int:disciplina_id>/', editar_disciplina, name='editar_disciplina'),

    path('login/', autentic.login_user, name='login'),
    path('logout/', autentic.logout_user, name='logout'),

    path('<str:site>/login/', autentic.login_user_withredirect, name = 'login_redirect'),
    path('<str:site>/logout/', autentic.logout_user_withredirect, name = 'logout_redirect'),

    path('docente/editar/<int:docente_id>/', editar_docente, name='editar_docente'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]