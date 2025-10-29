from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    """
    Paginación estándar que devuelve el formato esperado por el frontend:
    {
        "count": número total de elementos,
        "next": URL de la siguiente página,
        "previous": URL de la página anterior,
        "results": array con los resultados
    }
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


class CitasPagination(StandardResultsSetPagination):
    """
    Paginación específica para citas con un tamaño de página más pequeño
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50