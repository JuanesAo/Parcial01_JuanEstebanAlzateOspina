from django.urls import path
from .views import HomeView, FlightCreateView, FlightListView, FlightStatsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('registrar/', FlightCreateView.as_view(), name='flight_create'),
    path('listar/', FlightListView.as_view(), name='flight_list'),
    path('estadisticas/', FlightStatsView.as_view(), name='flight_stats'),
] 