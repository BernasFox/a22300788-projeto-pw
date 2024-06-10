from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def index_view(request):
    return show_all_view(request, 'banda')

#show
def show_view(request, tipo, nome_data):
    if tipo == 'album':
        data = Album.objects.get(id= nome_data)

    elif tipo == 'musica':
        data = Musica.objects.get(id= nome_data)

    else:
        data = Banda.objects.get(id = nome_data)

    content = {
        'tipo': tipo,
        'data': data,
        'id': nome_data
    }

    return render(request, "bandas/show.html", content)

# all
def show_all_view(request, tipo):
    if tipo == 'album':
        data = Album.objects.all().order_by('nome')

    elif tipo == 'musica':
        data = Musica.objects.all().order_by('titulo')

    else:
        data = Banda.objects.all().order_by('nome')

    context = {
        'tipo': tipo,
        'data': data,
    }
    return render(request, "bandas/show_all.html", context)

# Edit
@login_required
def edit_view(request, id_data, tipo):
    if tipo == "banda":
        data = Banda.objects.get(id = id_data)

        content = {
            'data': data,
            'tipo': tipo,
        }

        if request.method == 'POST':
            form = BandaForm(request.POST, request.FILES, instance=data)
            if form.is_valid():
                form.save()
                return redirect('bandas:show', tipo= 'banda', nome_data = id_data)
        else:
            form = BandaForm(instance=data)
        content['form'] = form

        return render(request, 'bandas/edit.html', content)

    elif tipo == "album":
        data = Album.objects.get(id = id_data)
        content = {
            'data': data,
            'tipo': tipo,
        }

        if request.method == 'POST':
            form = AlbumForm(request.POST, request.FILES, instance=data)
            if form.is_valid():
                form.save()
                return redirect('bandas:show', tipo= 'album', nome_data = id_data)
        else:
            form = AlbumForm(instance=data)
        content['form'] = form
        return render(request, 'bandas/edit.html', content)

    elif tipo == "musica":
        data = Musica.objects.get(id = id_data)
        content = {
            'data': data,
            'tipo': tipo,
        }

        if request.method == 'POST':
            form = MusicaForm(request.POST, request.FILES, instance=data)
            if form.is_valid():
                form.save()
                return redirect('bandas:show', tipo= 'musica', nome_data = id_data)
        else:
            form = MusicaForm(instance=data)

        content['form'] = form
        return render(request, 'bandas/edit.html', content)

    else:
        return redirect('bandas:bandas')

#inserir
@login_required
def insert_view(request, tipo):

    content = {
        'tipo':tipo,
    }

    if request.method == 'POST':
        if tipo == 'banda':
            nome_banda = request.POST.get('nome_banda')
            banda = Banda.objects.create(nome=nome_banda)
            return redirect('bandas:show', 'banda', banda.id)  # Redirecionar para uma página de sucesso

        elif tipo == 'album':
            nome_album = request.POST.get('nome_album')
            album = Album.objects.create(nome=nome_album)
            return redirect('bandas:show', 'album', album.id)  # Redirecionar para uma página de sucesso

        elif tipo == 'musica':
            titulo_musica = request.POST.get('titulo_musica')
            musica = Musica.objects.create(titulo=titulo_musica)
            return redirect('bandas:show', 'musica', musica.id)  # Redirecionar para uma página de sucesso

    # Passando o tipo para o contexto do template
    return render(request, 'bandas/insert.html', content)

#apagar
@login_required
def apagar_view(request, tipo):
    if tipo == 'album':
        context = {
            'tipo':'album',
            'data': Album.objects.all().order_by('nome'),
        }
        return render(request, "bandas/apagar.html", context)

    elif tipo == 'musica':
        context = {
            'tipo':'musica',
            'data': Musica.objects.all().order_by('titulo'),
        }
        return render(request, "bandas/apagar.html", context)

    elif tipo == 'banda':
        context = {
            'tipo':'banda',
            'data': Banda.objects.all().order_by('nome'),
        }
        return render(request, "bandas/apagar.html", context)

    else:
        render(request, "bandas/layout.html")

#funcoes
@login_required
def apagar(request, id_data, tipo):
    if tipo == 'banda':
        instance = get_object_or_404(Banda, id=id_data)
    elif tipo == 'album':
        instance = get_object_or_404(Album, id=id_data)
    elif tipo == 'musica':
        instance = get_object_or_404(Musica, id=id_data)
    else:
        # Handle invalid type
        return redirect('')  # Redirect to appropriate page

    # Delete the instance
    instance.delete()

    # Redirect to appropriate page
    if tipo == 'banda':
        return redirect('bandas:show_all', 'banda')

    elif tipo == 'album':
        return redirect('bandas:show_all', 'album')

    elif tipo == 'musica':
        return redirect('bandas:show_all', 'musica')








