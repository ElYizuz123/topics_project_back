from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'edad', 'genero')
    search_fields = ('nombre', 'apellido')
