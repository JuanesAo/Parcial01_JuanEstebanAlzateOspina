"""
URL principal del proyecto.

MVT: el proyecto delega rutas a la app `flights` usando `include`,
separando responsabilidades entre proyecto (composición de URLs) y app.
"""
from django.urls import path, include

urlpatterns = [
    # Rutas de la app de vuelos
    path('', include('flights.urls')),
]
