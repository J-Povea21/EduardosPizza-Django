from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import signing
from .forms import *


# Create your views here.
def index(request):
    # We clean any previous order token that may be in the session
    request.session['order_token'] = None

    context = {
        "customer_form": CustomerForm(),
        "order_form": OrderForm(),
        "pizza_form": PizzaForm(),
        "coupon_form": CouponRedemptionForm(),
    }

    return render(request, 'frontend/front-home.html', context)


def create_order(request):
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

            # We update the total value of the order with the pizza
            order.calculate_total_value()

            # Finally, we hash the order id and save it in the session as 'order_token'
            request.session['order_token'] = signing.dumps(order.id)

            return redirect('webapp:order-detail')
        else:
            return redirect('webapp:index')

    else:
        render(request, 'frontend/front-home.html')  # This is only a post view


def order_detail(request):
    # We get the token from the session
    order_token = request.session.get('order_token', None)

    # We get the order by the id with a try/except
    try:
        order = Order.objects.get(pk=signing.loads(order_token))
        context = {
            'order': order,
            'pizza': order.pizza,
            'ingredients': order.pizza.ingredients.all(),
            'deliveryman': order.deliveryman,
            'rating_form': RatingForm(),
        }
        return render(request, 'frontend/page-order-detail.html', context)

    except (Order.DoesNotExist, TypeError):
        return redirect('webapp:index')


def rate_deliveryman(request):
    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)

            try:
                order = Order.objects.get(pk=signing.loads(request.session.get('order_token', None)))
                rating.save(order=order)
                messages.success(request, '¡Gracias por calificar!')
                return redirect('webapp:index')
            except (Order.DoesNotExist, AttributeError):
                return redirect('webapp:index')

        else:
            return redirect('webapp:order-detail')
    else:
        return redirect('webapp:index')
