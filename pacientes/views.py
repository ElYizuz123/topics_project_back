from rest_framework import viewsets
from .models import Paciente
from rest_framework.pagination import PageNumberPagination 
from .serializers import PacienteSerializer
from rest_framework.permissions import IsAuthenticated

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10                 
    page_size_query_param = 'page_size' 
    max_page_size = 100 

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('id')
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination