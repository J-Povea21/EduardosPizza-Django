from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import *


# Here we use the LoginRequiredMixin to achieve the same result as the @login_required
# decorator. Thanks to the fact that a lot of views require the user to be logged in,
# we can use this class to avoid repeating and just display the information
class BaseListView(LoginRequiredMixin, ListView):
    login_url = 'ors:login'
    ordering = 'id'

    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class ReviewListView(BaseListView):
    model = Rating
    template_name = 'davur/reviews.html'
    title = 'Reseñas'


class OrderListView(BaseListView):
    model = Order
    template_name = 'davur/order_list.html'
    title = 'Órdenes'


class PizzaListView(BaseListView):
    model = Pizza
    template_name = 'davur/pizzas.html'
    title = 'Pizzas'


class CustomerListView(BaseListView):
    model = Customer
    template_name = 'davur/customers.html'
    title = 'Clientes'


class DeliverymanListView(BaseListView):
    model = Deliveryman
    template_name = 'davur/deliverymen.html'
    title = 'Repartidores'


class CouponListView(BaseListView):
    model = Coupon
    template_name = 'davur/coupons.html'
    title = 'Cupones'


class MassListView(BaseListView):
    model = Mass
    template_name = 'davur/masses.html'
    title = 'Masa'


class IngredientListView(BaseListView):
    model = Ingredient
    template_name = 'davur/ingredients.html'
    title = 'Ingredientes'


class SizeListView(BaseListView):
    model = Size
    template_name = 'davur/sizes.html'
    title = 'Tamaños'
