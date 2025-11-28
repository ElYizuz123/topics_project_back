from django.contrib import admin
from .models import RegistroDiario

@admin.register(RegistroDiario)
class RegistroDiarioAdmin(admin.ModelAdmin):
    list_display = ('cita', 'fecha', 'cumplio', 'dolor_ejecucion', 'dificultad_percibida')
    list_filter = ('cumplio', 'dificultad_percibida', 'fecha')
    search_fields = ('cita__paciente__nombre', 'cita__paciente__apellido', 'observaciones')
    
    fieldsets = (
        ('Información General', {
            'fields': ('cita', 'fecha', 'cumplio')
        }),
        ('Evaluación del Ejercicio', {
            'fields': ('dolor_ejecucion', 'dificultad_percibida', 'observaciones'),
        }),
    )
