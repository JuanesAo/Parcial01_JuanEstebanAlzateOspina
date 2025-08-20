"""
Capa de servicios del dominio de vuelos.

MVT: la lógica de negocio se mantiene fuera de las Views para que las vistas sean delgadas.
SOLID:

- Single Responsibility: cada función resuelve una responsabilidad clara (listar, calcular estadísticas).
- Open/Closed: podemos extender con nuevos cálculos/consultas sin modificar las vistas existentes.
"""
from decimal import Decimal
from typing import Dict, Any
from django.db.models import Avg, QuerySet

from .models import Flight, FlightType


def list_flights_ordered_by_price() -> QuerySet[Flight]:
    #Devuelve todos los vuelos ordenados de menor a mayor precio.
    
    return Flight.objects.all().order_by('price')


def calculate_flight_statistics() -> Dict[str, Any]:
    """Calcula estadísticas del dominio de vuelos.

    Retorna un diccionario con:
    - count_national: cantidad de vuelos con tipo Nacional
    - count_international: cantidad de vuelos con tipo Internacional
    - average_national_price: promedio del precio de vuelos Nacionales (o None si no hay)

    """
    count_national = Flight.objects.filter(type=FlightType.NACIONAL).count()
    count_international = Flight.objects.filter(type=FlightType.INTERNACIONAL).count()
    avg_national = Flight.objects.filter(type=FlightType.NACIONAL).aggregate(avg=Avg('price'))['avg']
    return {
        'count_national': count_national,
        'count_international': count_international,
        'average_national_price': Decimal(avg_national) if avg_national is not None else None,
    } 