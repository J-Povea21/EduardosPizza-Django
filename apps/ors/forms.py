from django import forms
from django.contrib.auth import authenticate
from .models import Deliveryman, Coupon, Mass, Ingredient, Size


# Here's a function to generate a response for the products forms like
# size, mass and ingredient. They all return the same response, so we
# can use this function to avoid repeating code.

def generate_product_response(redirect_page: str, has_errors: bool = False):
    if has_errors:
        return {'success': False, 'errors': ['El precio debe ser positivo']}
    else:
        return {'success': True, 'redirect_to': redirect_page}


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
        fields = ['name', 'cedula', 'active', 'phone_number']

        widgets = {
            'name': forms.TextInput,
            'cedula': forms.NumberInput,
            'phone_number': forms.TextInput,
            'active': forms.CheckboxInput,
        }

    def get_error_messages(self):
        error_list = []
        if self.errors.get('cedula'):
            error_list.append('La cédula debe ser positiva')
        return error_list

    def generate_response(self, has_errors: bool = False):
        if has_errors:
            return {'exists': True, 'errors': self.get_error_messages()}
        else:
            return {'exists': False, 'redirect_to': 'deliverymen'}


class CouponCreationForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'

        widgets = {
            'code': forms.TextInput,
            'discount': forms.NumberInput,
            'status': forms.Select,
        }

    def get_error_messages(self):
        error_list = []
        if self.errors.get('discount'):
            error_list.append('El descuento debe estar entre 0.1 y 0.3')
        elif self.errors.get('code'):
            error_list.append('El código ya existe')

        return error_list

    def generate_response(self, has_errors: bool = False):
        if has_errors:
            return {'success': False, 'errors': self.get_error_messages()}
        else:
            return {'success': True, 'redirect_to': 'coupons'}


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        widgets = {
            'name': forms.TextInput,
            'price_per_pizza': forms.NumberInput,
            'available': forms.CheckboxInput,
        }

    def generate_response(self, has_errors: bool = False):
        return generate_product_response('ingredients', has_errors)


class MassForm(forms.ModelForm):
    class Meta:
        model = Mass
        fields = '__all__'
        widgets = {
            'name': forms.TextInput,
            'price_per_pizza': forms.NumberInput,
            'available': forms.CheckboxInput,
        }

    def generate_response(self, has_errors: bool = False):
        return generate_product_response('masses', has_errors)


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        widgets = {
            'name': forms.TextInput,
            'price_per_pizza': forms.NumberInput,
            'available': forms.CheckboxInput,
        }

    def generate_response(self, has_errors: bool = False):
        return generate_product_response('sizes', has_errors)
