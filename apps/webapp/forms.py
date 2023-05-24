from django import forms
from django.core.exceptions import ValidationError
from apps.ors.models import *


def validate_coupon(value) -> float:
    discount = 0
    try:
        coupon = Coupon.objects.get(code=value)
        discount = coupon.discount
    except Coupon.DoesNotExist:
        raise ValidationError('El cupón ingresado no existe')
    else:
        if coupon.status == 'CANJEADO':
            raise ValidationError('El cupón ingresado ya fue canjeado')
        elif coupon.status == 'DISPONIBLE':
            return discount


## FORMS ##

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        labels = {
            'name': 'Nombre completo*',
            'cedula': 'Cédula*',
            'address': 'Dirección de entrega*',
            'phone_number': 'Número de teléfono*',
        }


class CouponRedemptionForm(forms.Form):
    code = forms.CharField(
        max_length=7,
        min_length=7,
        validators=[validate_coupon],
        label='Código de cupón',
        required=False,
    )


class OrderForm(forms.ModelForm):
    coupon_code = CouponRedemptionForm()

    class Meta:
        model = Order

        fields = ['payment_method']

        labels = {
            'payment_method': 'Método de pago',
        }


class PizzaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)

        # Update the widget choices based on the current availability of ingredients and mass types
        self.fields['ingredients'].widget.choices = Ingredient.objects.filter(available=True).values_list('id', 'name')
        self.fields['mass_type'].widget.choices = Mass.objects.filter(available=True).values_list('id', 'name')

    class Meta:
        model = Pizza
        fields = ['size', 'mass_type', 'ingredients']
        labels = {
            'size': 'Tamaño',
            'mass_type': 'Masa',
            'ingredients': 'Ingredientes',
        }
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple,
            'mass_type': forms.Select,
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating

        exclude = ['order']

        labels = {
            'rating_value': 'Calificación',
            'message': 'Mensaje (opcional)',
        }
