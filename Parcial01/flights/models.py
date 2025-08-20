from django.db import models
from django.core.validators import MinValueValidator


class FlightType(models.TextChoices):
    # Tipos de vuelo del dominio.
    NACIONAL = 'Nacional', 'Nacional'
    INTERNACIONAL = 'Internacional', 'Internacional'


class Flight(models.Model):
    """
    Campos:
    - name: nombre del vuelo
    - type: restringido a `FlightType`
    - price: precio positivo con dos decimales

    Notas:
    - MVT (Model): representa la tabla en BD; las migraciones crean la estructura.
    - Meta.ordering: lista por precio ascendente.
    """
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=20, choices=FlightType.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    class Meta:
        ordering = ['price']

    def __str__(self) -> str:
        return f"{self.name} ({self.type}) - ${self.price}"
