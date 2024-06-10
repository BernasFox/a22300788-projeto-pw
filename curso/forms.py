from django import forms
from .models import *

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'ano', 'semestre', 'ects', 'curricularIUnitReadableCode', 'area_cientifica', 'projetos']

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nome', 'disciplinas']