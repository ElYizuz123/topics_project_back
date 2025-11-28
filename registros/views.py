from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import RegistroDiario
from .serializers import RegistroDiarioSerializer


class RegistroDiarioViewSet(viewsets.ModelViewSet):
    queryset = RegistroDiario.objects.all().order_by('-fecha')
    serializer_class = RegistroDiarioSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['fecha', 'dolor_ejecucion']
    ordering = ['-fecha']

    def get_queryset(self):
        qs = super().get_queryset()
        
        # Filtro por cita
        cita_id = self.request.query_params.get('cita')
        if cita_id:
            qs = qs.filter(cita_id=cita_id)
        
        # Filtro por cumplimiento
        cumplio = self.request.query_params.get('cumplio')
        if cumplio is not None:
            qs = qs.filter(cumplio=cumplio.lower() in ['true', '1', 'yes'])
        
        # Filtro por dificultad percibida
        dificultad = self.request.query_params.get('dificultad_percibida')
        if dificultad:
            qs = qs.filter(dificultad_percibida=dificultad)
        
        return qs
