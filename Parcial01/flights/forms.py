"""
Formularios para la capa de presentación.

MVT: los Forms encapsulan validaciones y transformación de datos de entrada.
SOLID (SRP): las reglas de validación residen aquí, no en las Views. (concepto visto en clase)
"""
from django import forms
from .models import Flight, FlightType


class FlightForm(forms.ModelForm):
    # Formulario para crear/editar `Flight` con validaciones explícitas.
    class Meta:
        model = Flight
        fields = ['name', 'type', 'price']
        widgets = {
            'type': forms.Select(choices=FlightType.choices),
        }

    def clean_name(self):
        # Validael nombre no esté vacío y remueve espacios extra.
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('El nombre es obligatorio.')
        return name

    def clean_type(self):
        # Valida que el tipo pertenezca a los valores de `FlightType`.
        type_value = self.cleaned_data.get('type')
        valid_values = {choice_value for choice_value, _ in FlightType.choices}
        if type_value not in valid_values:
            raise forms.ValidationError('Tipo de vuelo inválido.')
        return type_value

    def clean_price(self):
        # Valida que el precio sea un número positivo mayor que 0.
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise forms.ValidationError('El precio debe ser mayor que 0.')
        return price 