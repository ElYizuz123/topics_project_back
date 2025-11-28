from django.db import models
from pacientes.models import Paciente

class Cita(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('asistida', 'Asistida'),
        ('cancelada', 'Cancelada'),
    )
    
    TIPOS = (
        ('primera', 'Primera vez'),
        ('seguimiento', 'Seguimiento'),
    )
    
    INTENSIDADES = (
        ('baja', 'Baja'),
        ('moderada', 'Moderada'),
        ('alta', 'Alta'),
    )

    paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE, 
        related_name='citas'
    )
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=255)
    tipo = models.CharField(
        max_length=20, 
        choices=TIPOS, 
        default='primera'
    )
    estado = models.CharField(
        max_length=20, 
        choices=ESTADOS, 
        default='pendiente'
    )
    
    # Nuevos campos de ejercicio y seguimiento
    tipo_ejercicio = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        help_text='Tipo de ejercicio realizado'
    )
    repeticiones = models.IntegerField(
        blank=True, 
        null=True,
        help_text='Número de repeticiones'
    )
    tiempo = models.IntegerField(
        blank=True, 
        null=True,
        help_text='Tiempo en minutos'
    )
    intensidad = models.CharField(
        max_length=20,
        choices=INTENSIDADES,
        blank=True,
        null=True,
        help_text='Intensidad del ejercicio'
    )
    frecuencia_semanal = models.IntegerField(
        blank=True,
        null=True,
        help_text='Días de ejercicio por semana'
    )
    progreso_positivo = models.BooleanField(
        default=False,
        help_text='¿Hubo progreso positivo?'
    )
    imc = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Índice de Masa Corporal'
    )
    porcentaje_grasa_corporal = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Porcentaje de grasa corporal'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha', '-hora']

    def __str__(self):
        return f'{self.paciente} - {self.fecha} {self.hora}'