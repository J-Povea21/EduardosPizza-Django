from django.urls import path, include
from . import views


urlpatterns = [
    path('create_order', views.create_order, name='create_order'),
    path('order_in_progress', views.order_in_progress, name='order_in_progress'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('statistics', views.statistics, name='statistics'),
    path('reviews', views.reviews, name='reviews'),
    path('customers', views.customers, name='customers'),
    path('order_list', views.order_list, name='order_list'),
    path('products/masses', views.masses, name='masses'),
    path('products/ingredients', views.ingredients, name='ingredients'),
    path('products/ingredients/<int:ingredient_id>', views.edit_ingredient, name='edit_ingredient'),
    path('test', views.test, name='test'),
]
