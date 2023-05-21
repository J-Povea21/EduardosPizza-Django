from django import forms
from django.core.exceptions import ValidationError

from .models import *


#### form Validator ####

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


#### Forms ####
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


class DeliverymanCreationForm(forms.ModelForm):
    class Meta:
        model = Deliveryman
        fields = ['name', 'cedula', 'active']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-rounded ',
                                           'placeholder': 'Ej: Eduardo Angulo',
                                           'maxlength': 30,
                                           'minlength': 2,
                                           }),

            'cedula': forms.NumberInput(attrs={'class': 'form-control input-rounded '}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check custom-checkbox mb-3 checkbox-info check-lg'}),
        }


class CouponCreationForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'

        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control input-rounded ',
                                           'placeholder': 'Ej: DST1234',
                                           'maxlength': 7,
                                           'minlength': 7}),
            'discount': forms.NumberInput(attrs={'class': 'form-control input-rounded ',
                                                 'min': 0.1,
                                                 'max': 0.3,}),
            'status': forms.Select(attrs={'class': 'form-select'}),
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


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

        labels = {
            'name': 'Nombre',
            'price_per_pizza': 'Precio',
            'available': 'Disponible',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-rounded ', 'maxlength': 30, 'minlength': 2}),
            'price_per_pizza': forms.NumberInput(attrs={'class': 'form-control input-rounded ', 'min': 1}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check custom-checkbox mb-3 checkbox-info check-lg'}),
        }


class MassForm(forms.ModelForm):
    class Meta:
        model = Mass
        fields = '__all__'

        labels = {
            'name': 'Nombre',
            'price_per_pizza': 'Precio',
            'available': 'Disponible',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-rounded '}),
            'price_per_pizza': forms.NumberInput(attrs={'class': 'form-control input-rounded ', 'min': 0}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check custom-checkbox mb-3 checkbox-info check-lg'}),
        }
