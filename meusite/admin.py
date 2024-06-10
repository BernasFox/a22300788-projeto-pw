from django.contrib import admin

# Register your models here.
from .models import Tipo, Trabalho

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Trabalho)
