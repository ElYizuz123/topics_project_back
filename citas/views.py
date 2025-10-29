from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Cita
from .serializers import CitaSerializer
from healtyapi.pagination import CitasPagination

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CitasPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['motivo', 'paciente__nombre', 'paciente__apellidos']
    ordering_fields = ['fecha', 'hora', 'created_at']
    ordering = ['-fecha', '-hora']  # Orden por defecto: más recientes primero

    def get_queryset(self):
        qs = super().get_queryset()
        
        # Filtro por paciente (mantenido para compatibilidad)
        paciente_id = self.request.query_params.get('paciente') 
        if paciente_id:
            qs = qs.filter(paciente_id=paciente_id)
        
        # Filtro por estado
        estado = self.request.query_params.get('estado')
        if estado:
            qs = qs.filter(estado=estado)
        
        # Filtro por tipo
        tipo = self.request.query_params.get('tipo')
        if tipo:
            qs = qs.filter(tipo=tipo)
        
        return qs