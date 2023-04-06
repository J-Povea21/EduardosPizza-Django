from django.shortcuts import render, redirect
from .forms import OrderForm, CustomerForm, PizzaForm
from .models import Order


# Create your views here.

def admin_panel(request):
    return render(request, 'admin_panel.html')


def create_order(request):
    if request.method == "POST":

        # 1. Se validan los datos enviados por el cliente
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
            customer = customer_form.save()

            # 2. Se validan los datos de la orden
            order_form = OrderForm(request.POST)

            if order_form.is_valid():

                order = order_form.save(commit=False)
                order.save(customer = customer)

                pizza_form = PizzaForm(request.POST)

                if pizza_form.is_valid():
                    pizza = pizza_form.save(commit=False)
                    ingredients = pizza_form.cleaned_data['ingredients']

                    pizza.save(order=order, ingredients=ingredients)

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
