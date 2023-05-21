from django.urls import path
from . import views


urlpatterns = [
    path('create_order', views.create_order, name='create_order'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('statistics', views.statistics, name='statistics'),
    path('reviews', views.reviews, name='reviews'),
    path('customers', views.customers, name='customers'),

    path('deliverymen', views.deliverymen, name='deliverymen'),
    path('deliverymen/create_deliveryman', views.create_deliveryman, name='create_deliveryman'),
    path('deliverymen/edit_deliveryman/<int:deliveryman_id>', views.edit_deliveryman, name='edit_deliveryman'),

    path('order_list', views.order_list, name='order_list'),
    path('pizzas', views.pizzas, name='pizzas'),

    path('coupons', views.coupons, name='coupons'),
    path('coupons/create_coupon', views.create_coupon, name='create_coupon'),
    path('coupons/edit_coupon/<int:coupon_id>', views.edit_coupon, name='edit_coupon'),

    path('products/masses', views.masses, name='masses'),
    path('products/masses/create_mass', views.create_mass, name='create_mass'),
    path('products/masses/<int:mass_id>', views.edit_mass, name='edit_mass'),

    path('products/ingredients', views.ingredients, name='ingredients'),
    path('products/ingredients/create_ingredient', views.create_ingredient, name='create_ingredient'),
    path('products/ingredients/<int:ingredient_id>', views.edit_ingredient, name='edit_ingredient'),

    path('test', views.test, name='test'),
]
