from django.shortcuts import render

def index_view(request):
    return render(request, "novaapp/index.html")

def sobre_view(request):
    return render(request, "novaapp/sobre.html")

def sobremim_view(request):
    return render(request, "novaapp/sobremim.html")

def blank_view(request):
    return render(request, "novaapp/index.html")
