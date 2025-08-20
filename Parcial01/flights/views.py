"""
Vistas (MVT - View) para la gestión de vuelos.

Principios aplicados:
- MVT: las Views orquestan la interacción HTTP y delegan la lógica de dominio a `services`.
- SOLID (SRP): las Views no contienen reglas de negocio; usan formularios y servicios.
"""
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from .forms import FlightForm
from .models import Flight
from . import services


class HomeView(TemplateView):
    """Página de inicio: ofrece navegación a registrar, listar y estadísticas.
    Parte de MVT (View): renderiza un template sin lógica de dominio.
    """
    template_name = 'flights/home.html'


class FlightCreateView(CreateView):
    """Registro de vuelos a través de `FlightForm`.

    - MVT: View + Form; las validaciones viven en el formulario.
    - SOLID: la vista se mantiene delgada (SRP) y delega validación al Form.
    """
    model = Flight
    form_class = FlightForm
    template_name = 'flights/flight_form.html'
    success_url = reverse_lazy('flight_list')


class FlightListView(ListView):
    """Listado de vuelos.

    Delegamos en `services.list_flights_ordered_by_price` el criterio de ordenación
    para cumplir SRP en la vista y Open/Closed en la lógica de listado.
    """
    model = Flight
    template_name = 'flights/flight_list.html'
    context_object_name = 'flights'

    def get_queryset(self):
        """Obtiene el queryset desde la capa de servicios (reglas de negocio afuera)."""
        return services.list_flights_ordered_by_price()


class FlightStatsView(TemplateView):
    """Estadísticas de vuelos.

    La obtención de métricas se delega a `services.calculate_flight_statistics`
    para mantener la vista enfocada en presentación.
    """
    template_name = 'flights/flight_stats.html'

    def get_context_data(self, **kwargs):
        """Inyecta las estadísticas calculadas por la capa de servicios en el contexto."""
        context = super().get_context_data(**kwargs)
        stats = services.calculate_flight_statistics()
        context.update(stats)
        return context
