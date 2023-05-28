from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('reviews', views.ReviewListView.as_view(), name='reviews'),
    path('customers', views.CustomerListView.as_view(), name='customers'),

    path('deliverymen', views.DeliverymanListView.as_view(), name='deliverymen'),
    path('deliverymen/create_deliveryman', views.create_deliveryman, name='create_deliveryman'),
    path('deliverymen/edit_deliveryman/<int:deliveryman_id>', views.edit_deliveryman, name='edit_deliveryman'),

    path('order_list', views.OrderListView.as_view(), name='order_list'),
    path('pizzas', views.PizzaListView.as_view(), name='pizzas'),

    path('coupons', views.CouponListView.as_view(), name='coupons'),
    path('coupons/create_coupon', views.create_coupon, name='create_coupon'),
    path('coupons/edit_coupon/<int:coupon_id>', views.edit_coupon, name='edit_coupon'),

    path('products/sizes', views.SizeListView.as_view(), name='sizes'),
    path('products/sizes/create_size', views.create_size, name='create-size'),

    path('products/masses', views.MassListView.as_view(), name='masses'),
    path('products/masses/create_mass', views.create_mass, name='create_mass'),
    path('products/masses/<int:mass_id>', views.edit_mass, name='edit_mass'),

    path('products/ingredients', views.IngredientListView.as_view(), name='ingredients'),
    path('products/ingredients/create_ingredient', views.create_ingredient, name='create_ingredient'),
    path('products/ingredients/<int:ingredient_id>', views.edit_ingredient, name='edit_ingredient'),
]
