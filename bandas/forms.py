from django import forms
from .models import *

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nome', 'foto', 'album']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nome', 'capa', 'musicas']

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'link', 'foto', 'biografia']
        help_texts = { 'biografia': '<br>Insira uma breve biografia de 4-5 linhas.',
                        'titulo': '<br>Escreva o titulo da musica',
                        'link': '<br>Insira o link da musica',
                        'foto': '<br>Inserir Imagem',
                    }
