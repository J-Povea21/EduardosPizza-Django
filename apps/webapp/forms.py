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


def get_all_error_messages(*forms):
    errors = []
    for form in forms:
        for field in form:
            for error in field.errors:
                if error not in errors and error != '':
                    errors.append(f"*{field.name}: {error} \n")
    return errors


## FORMS ##

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


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

        # First we get the available mass types and ingredients
        ingredients = Ingredient.objects.filter(available=True).values_list('id', 'name')
        mass_types = Mass.objects.filter(available=True).values_list('id', 'name')
        size_types = Size.objects.filter(available=True).values_list('id', 'name')

        # Then we create the choices for the select inputs
        self.fields['ingredients'].widget.choices = ingredients

        self.fields['mass_type'].widget.choices = mass_types

        self.fields['size'].widget.choices = size_types

        # And finally we create three dictionaries where we store the prices of ingredients, sizes and masses
        self.__generate_dicts()

    class Meta:
        model = Pizza
        fields = ['size', 'mass_type', 'ingredients']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple,
            'mass_type': forms.Select,
        }

    def __generate_dicts(self):
        self.ingredients_prices = dict(Ingredient.objects.filter(available=True).values_list('id', 'price_per_pizza'))
        self.mass_types_prices = dict(Mass.objects.filter(available=True).values_list('id', 'price_per_pizza'))
        self.size_prices = dict(Size.objects.filter(available=True).values_list('id', 'price_per_pizza'))


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating

        exclude = ['order']

        labels = {
            'rating_value': 'Calificación',
            'message': 'Mensaje (opcional)',
        }
