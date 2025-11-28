from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'hora', 'tipo', 'estado', 'progreso_positivo', 'imc')
    list_filter = ('estado', 'tipo', 'fecha', 'intensidad', 'progreso_positivo')
    search_fields = ('paciente__nombre', 'paciente__apellido', 'motivo', 'tipo_ejercicio')
    
    fieldsets = (
        ('Información General', {
            'fields': ('paciente', 'fecha', 'hora', 'motivo', 'tipo', 'estado')
        }),
        ('Datos de Ejercicio', {
            'fields': ('tipo_ejercicio', 'repeticiones', 'tiempo', 'intensidad', 'frecuencia_semanal'),
            'classes': ('collapse',)
        }),
        ('Métricas de Salud', {
            'fields': ('imc', 'porcentaje_grasa_corporal', 'progreso_positivo'),
            'classes': ('collapse',)
        }),
    )