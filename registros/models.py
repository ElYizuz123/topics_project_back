from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from citas.models import Cita


class RegistroDiario(models.Model):
    DIFICULTAD_CHOICES = (
        ('facil', 'Fácil'),
        ('moderado', 'Moderado'),
        ('dificil', 'Difícil'),
    )
    
    cita = models.ForeignKey(
        Cita,
        on_delete=models.CASCADE,
        related_name='registros'
    )
    fecha = models.DateField()

    cumplio = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)
    
    # Nuevos campos
    dolor_ejecucion = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=True,
        null=True,
        help_text='Nivel de dolor durante el ejercicio (0-10)'
    )
    dificultad_percibida = models.CharField(
        max_length=20,
        choices=DIFICULTAD_CHOICES,
        blank=True,
        null=True,
        help_text='Dificultad percibida del ejercicio'
    )

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.cita} - {self.fecha}"
