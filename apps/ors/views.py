from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import OrderForm, CustomerForm, PizzaForm
from .models import Order, Coupon


# Create your views here.

def admin_panel(request):
    return render(request, 'admin_panel.html')


def create_order(request, **kwargs):
    if request.method == "POST":

        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)
        pizza_form = PizzaForm(request.POST)

        # We check if the coupon code is valid
        coupon_code = request.POST['coupon_code']
        discount = 0
        if coupon_code != '':
            try:

                coupon = Coupon.objects.get(code=coupon_code, status='DISPONIBLE')
                discount = coupon.discount
                coupon.status = 'CANJEADO'
                coupon.save()
            except Coupon.DoesNotExist:
                messages.error(request, 'El cupón no existe o ya fue canjeado')

        forms_are_valid = customer_form.is_valid() & order_form.is_valid() \
                          & pizza_form.is_valid()

        if forms_are_valid:
            # We save the customer first, then we link it to the order
            customer = customer_form.save()
            order = order_form.save(commit=False)

            order.save(customer=customer, coupon_discount=discount)

            # We save the pizza with the ingredients and link the order to it
            pizza = pizza_form.save(commit=False)
            ingredients = pizza_form.cleaned_data['ingredients']

            pizza.save(order=order, ingredients=ingredients)

            # And finally we update the total value of the order with the pizza
            order.calculate_total_value()

            return redirect('create_order')
    else:
        customer_form = CustomerForm()
        order_form = OrderForm()
        pizza_form = PizzaForm()

    return render(request, 'create_order.html', {
        'pizza_form': pizza_form,
        'customer_form': customer_form,
        'order_form': order_form
    })
