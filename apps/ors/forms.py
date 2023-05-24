from django import forms
from django.contrib.auth import authenticate
from .models import Deliveryman, Coupon, Mass, Ingredient


#### Forms ####

class LoginForm(forms.Form):

    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


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
                                                 'max': 0.3, }),
            'status': forms.Select(attrs={'class': 'form-select'}),
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
