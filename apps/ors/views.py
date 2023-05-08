from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, CustomerForm, PizzaForm, RatingForm, CouponForm, IngredientForm
from .models import Order, Coupon, Ingredient, Rating, Customer


# Create your views here.

def admin_panel(request):
    return render(request, 'davur/statistics.html')


def statistics(request):
    return render(request, 'davur/statistics.html')


def reviews(request):

    context = {
        'review_list': Rating.objects.all(),
        'title': 'Reseñas',
    }

    return render(request, 'davur/reviews.html',context= context)


def order_list(request):

    context = {
        'orders': Order.objects.all(),
        'title': 'Órdenes',
    }

    return render(request, 'davur/order_list.html', context=context)


def customers(request):

    context = {
        'customers': Customer.objects.all(),
        'title': 'Clientes',
    }

    return render(request, 'davur/customers.html', context=context)


def masses(request):
    return render(request, 'davur/masses.html')


def ingredients(request):

    context = {
        'ingredients': Ingredient.objects.all(),
        'title': 'Ingredientes',
    }

    return render(request, 'davur/ingredients.html', context=context)



def edit_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    print('working')
    if request.method == 'POST':
        # Populate the ingredient form with the request data
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            # Save the changes to the database
            form.save()
            return redirect('ingredients')
    else:
        # Populate the ingredient form with the current data
        form = IngredientForm(instance=ingredient)

    # Render the template with the form
    return render(request, 'davur/ingredients.html', {'form': form, 'ingredient': ingredient})


def create_order(request, **kwargs):
    if request.method == "POST":

        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)
        pizza_form = PizzaForm(request.POST)
        coupon_form = CouponForm(request.POST)

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

            return redirect('order_in_progress')
    else:
        customer_form = CustomerForm()
        order_form = OrderForm()
        pizza_form = PizzaForm()
        coupon_form = CouponForm()

    return render(request, 'create_order.html', {
        'pizza_form': pizza_form,
        'customer_form': customer_form,
        'order_form': order_form,
        'coupon_form': coupon_form
    })


def test(request):
    return render(request, 'frontend/front-home.html')


def order_in_progress(request):
    if request.method == "POST":

        # We get the latest order because we know is the one we are working on
        order = Order.objects.latest('id')
        rating_form = RatingForm(request.POST)

        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.save(order=order)
            return redirect('create_order')
    else:
        rating_form = RatingForm()
    return render(request, 'order_in_progress.html', {'rating_form': rating_form})
