# API de Citas con Paginación

## Formato de Respuesta

Todas las respuestas de la API de citas ahora incluyen paginación con el siguiente formato:

```json
{
  "count": 25,
  "next": "http://localhost:8000/api/citas/?page=3",
  "previous": "http://localhost:8000/api/citas/?page=1",
  "results": [
    {
      "id": 1,
      "paciente": 1,
      "fecha": "2025-10-28",
      "hora": "10:30:00",
      "motivo": "Consulta de seguimiento",
      "tipo": "seguimiento",
      "estado": "pendiente",
      "created_at": "2025-10-28T10:00:00Z"
    }
    // ... más citas
  ]
}
```

## Parámetros de Consulta

### Paginación
- `page`: Número de página (por defecto: 1)
- `page_size`: Elementos por página (por defecto: 5, máximo: 50)

### Filtros
- `paciente`: ID del paciente
- `estado`: Estado de la cita (pendiente, asistida, cancelada)
- `tipo`: Tipo de cita (primera, seguimiento)

### Búsqueda
- `search`: Buscar en motivo, nombre y apellidos del paciente

### Ordenamiento
- `ordering`: Campo por el que ordenar (fecha, hora, created_at)
- Por defecto se ordena por `-fecha,-hora` (más recientes primero)

## Ejemplos de Uso

### Obtener todas las citas (primera página)
```
GET /api/citas/
```

### Obtener página específica
```
GET /api/citas/?page=2
```

### Cambiar tamaño de página
```
GET /api/citas/?page_size=10
```

### Filtrar por paciente
```
GET /api/citas/?paciente=1
```

### Filtrar por estado
```
GET /api/citas/?estado=pendiente
```

### Combinar filtros
```
GET /api/citas/?paciente=1&estado=pendiente&page_size=20
```

### Buscar citas
```
GET /api/citas/?search=dolor
```

### Ordenar por fecha ascendente
```
GET /api/citas/?ordering=fecha
```

### Ordenar por fecha descendente
```
GET /api/citas/?ordering=-fecha
```

## Cambios Implementados

1. **Paginación Global**: Configurada en `settings.py` con `StandardResultsSetPagination`
2. **Paginación Específica para Citas**: `CitasPagination` con 5 elementos por página
3. **Filtros Mejorados**: Estado, tipo, paciente
4. **Búsqueda**: En motivo y datos del paciente
5. **Ordenamiento**: Por fecha, hora, fecha de creación
6. **Compatibilidad**: Mantiene el filtro original por paciente