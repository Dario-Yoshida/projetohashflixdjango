from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

campo = list(UserAdmin.fieldsets)
campo.append(
    ("Historico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campo)
# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
