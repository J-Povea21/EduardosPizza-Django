from django import forms
from .models import Order, Customer, Pizza


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        labels = {
            'name': 'Escribe tu nombre',
            'cedula': 'Escrite tu cédula',
            'phone_number': 'Escrite tu teléfono',
            'address': 'Indica tu dirección',
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        exclude = ['discount', 'total_value',
                   'domicile_price', 'date', 'customer_id', 'deliveryman',
                   'destination']


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza

        exclude = ['price', 'price_per_size', 'price_per_mass', 'order_reference']
