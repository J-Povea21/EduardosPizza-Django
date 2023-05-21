from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.

## General information of the bussiness ##
def admin_panel(request):
    return render(request, 'davur/statistics.html')


def statistics(request):
    return render(request, 'davur/statistics.html')


def reviews(request):
    context = {
        'review_list': Rating.objects.all(),
        'title': 'Reseñas',
    }

    return render(request, 'davur/reviews.html', context=context)


def order_list(request):
    context = {
        'orders': Order.objects.all(),
        'title': 'Órdenes',
    }

    return render(request, 'davur/order_list.html', context=context)


def pizzas(request):
    context = {
        'pizzas': Pizza.objects.all(),
        'title': 'Pizzas',
    }

    return render(request, 'davur/pizzas.html', context=context)


def customers(request):
    context = {
        'customers': Customer.objects.all(),
        'title': 'Clientes',
    }

    return render(request, 'davur/customers.html', context=context)


def deliverymen(request):
    context = {
        'deliverymen': Deliveryman.objects.all(),
        'title': 'Repartidores',
    }
    return render(request, 'davur/deliverymen.html', context=context)


def coupons(request):
    context = {
        'coupons': Coupon.objects.all().order_by('id'),
        'title': 'Cupones',
    }

    return render(request, 'davur/coupons.html', context=context)


## Products of the bussiness ##

def masses(request):
    context = {
        'masses': Mass.objects.all(),
        'title': 'Masas',
    }
    return render(request, 'davur/masses.html', context=context)


def ingredients(request):
    context = {
        'ingredients': Ingredient.objects.all().order_by('id'),
        'title': 'Ingredientes',
    }

    return render(request, 'davur/ingredients.html', context=context)


## CRUD of the products ##

def create_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ors:ingredients')
    else:
        form = IngredientForm()

    return render(request, 'davur/create/create_ingredient.html', {'form': form})


def edit_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)

        if form.is_valid():
            # Update the ingredient with the new data
            ingredient.name = form.cleaned_data['name']
            ingredient.price_per_pizza = form.cleaned_data['price_per_pizza']
            ingredient.available = form.cleaned_data['available']

            ingredient.save(update_fields=['name', 'price_per_pizza', 'available'])
            return redirect('ors:ingredients')
    else:
        # Populate the ingredient form with the current data
        form = IngredientForm(instance=ingredient)

    # Render the template with the form
    return render(request, 'davur/update/edit_ingredient.html', {'form': form, 'ingredient': ingredient})


def create_mass(request):
    if request.method == 'POST':
        form = MassForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ors:masses')
    else:
        form = MassForm()
    return render(request, 'davur/create/create_mass.html', {'form': form})


def edit_mass(request, mass_id):
    mass = Mass.objects.get(pk=mass_id)
    if request.method == 'POST':
        form = MassForm(request.POST, instance=mass)

        if form.is_valid():
            # Update the mass with the new data
            mass.name = form.cleaned_data['name']
            mass.price = form.cleaned_data['price']
            mass.available = form.cleaned_data['available']

            mass.save(update_fields=['name', 'price', 'available'])
            return redirect('ors:masses')
    else:
        # Populate the mass form with the current data
        form = MassForm(instance=mass)

    return render(request, 'davur/update/edit_mass.html', {'form': form, 'mass': mass})


def create_deliveryman(request):
    if request.method == 'POST':
        form = DeliverymanCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({'exists': False})  # Cedula is valid
        else:
            return JsonResponse({'exists': True, 'errors': form.errors})  # Cedula already exists
    else:
        form = DeliverymanCreationForm()

    return render(request, 'davur/create/create_deliveryman.html', context={'form': form})


def edit_deliveryman(request, deliveryman_id):
    # We get the deliveryman with the given id
    deliveryman = Deliveryman.objects.get(pk=deliveryman_id)

    if request.method == 'POST':
        form = DeliverymanCreationForm(request.POST, instance=deliveryman)

        if form.is_valid():
            deliveryman.name = form.cleaned_data['name']
            deliveryman.cedula = form.cleaned_data['cedula']

            deliveryman.save(update_fields=['name', 'cedula'])
            return JsonResponse({'exists': False})  # Cedula is valid
        else:
            return JsonResponse({'exists': True, 'errors': form.errors})  # Cedula already exists
    else:
        form = DeliverymanCreationForm(instance=deliveryman)

    return render(request, 'davur/update/edit_deliveryman.html', {'form': form, 'deliveryman': deliveryman})


def create_coupon(request):
    if request.method == 'POST':
        form = CouponCreationForm(request.POST)

        if form.is_valid():

            coupon_already_exists = Coupon.objects.filter(code=form.cleaned_data['code']) \
                .exists()

            if coupon_already_exists:
                return JsonResponse({'exists': True})  # Coupon code already exists
            else:
                # Once we check the coupon is valid, we save it
                form.save()
                return JsonResponse({'exists': False})  # Coupon code is valid
    else:
        form = CouponCreationForm()

    return render(request, 'davur/create/create_coupon.html', context={'form': form})


def edit_coupon(request, coupon_id):
    coupon = Coupon.objects.get(pk=coupon_id)
    if request.method == 'POST':
        form = CouponCreationForm(request.POST, instance=coupon)

        if form.is_valid():
            # Update the coupon with the new data
            coupon.code = form.cleaned_data['code']
            coupon.discount = form.cleaned_data['discount']
            coupon.status = form.cleaned_data['status']

            coupon.save(update_fields=['code', 'discount', 'status'])
            return redirect('ors:coupons')
    else:
        # Populate the coupon form with the current data
        form = CouponCreationForm(instance=coupon)

    # Render the template with the form
    return render(request, 'davur/update/edit_coupon.html', {'form': form, 'coupon': coupon})


def create_order(request, **kwargs):
    if request.method == "POST":

        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)
        pizza_form = PizzaForm(request.POST)
        coupon_form = CouponRedemptionForm(request.POST)

        forms_are_valid = customer_form.is_valid() & order_form.is_valid() \
                          & pizza_form.is_valid() & coupon_form.is_valid()

        if forms_are_valid:
            # We save the customer first, then we link it to the order
            customer = customer_form.save()
            order = order_form.save(commit=False)

            # In case a coupon was given, we update his status and apply it to the order
            coupon = None
            if coupon_form.cleaned_data['code'] != '':
                coupon = Coupon.objects.get(code=coupon_form.cleaned_data['code'])

            order.save(customer=customer, coupon=coupon)

            # We save the pizza with the ingredients and link the order to it
            pizza = pizza_form.save(commit=False)
            ingredients = pizza_form.cleaned_data['ingredients']

            pizza.save(order=order, ingredients=ingredients)

            # And finally we update the total value of the order with the pizza
            order.calculate_total_value()

            return redirect('webapp:index')
    else:
        customer_form = CustomerForm()
        order_form = OrderForm()
        pizza_form = PizzaForm()
        coupon_form = CouponRedemptionForm()

    return render(request, 'create_order.html', {
        'pizza_form': pizza_form,
        'customer_form': customer_form,
        'order_form': order_form,
        'coupon_form': coupon_form
    })


def test(request):
    return render(request, 'frontend/front-home.html')
