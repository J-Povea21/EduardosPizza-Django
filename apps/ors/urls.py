from django.urls import path
from . import views, list_views


urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

    path('admin_panel', views.admin_panel, name='admin-panel'),
    path('reviews', list_views.ReviewListView.as_view(), name='reviews'),
    path('customers', list_views.CustomerListView.as_view(), name='customers'),

    path('deliverymen', list_views.DeliverymanListView.as_view(), name='deliverymen'),
    path('deliverymen/create_deliveryman', views.create_deliveryman, name='create-deliveryman'),
    path('deliverymen/edit_deliveryman/<int:deliveryman_id>', views.edit_deliveryman, name='edit-deliveryman'),

    path('order_list', list_views.OrderListView.as_view(), name='order-list'),
    path('pizzas', list_views.PizzaListView.as_view(), name='pizzas'),

    path('coupons', list_views.CouponListView.as_view(), name='coupons'),
    path('coupons/create-coupon', views.create_coupon, name='create-coupon'),
    path('coupons/edit-coupon/<int:coupon_id>', views.edit_coupon, name='edit-coupon'),

    path('products/sizes', list_views.SizeListView.as_view(), name='sizes'),
    path('products/sizes/create_size', views.create_size, name='create-size'),
    path('products/sizes/<int:size_id>', views.edit_size, name='edit-size'),

    path('products/masses', list_views.MassListView.as_view(), name='masses'),
    path('products/masses/create_mass', views.create_mass, name='create-mass'),
    path('products/masses/<int:mass_id>', views.edit_mass, name='edit-mass'),

    path('products/ingredients', list_views.IngredientListView.as_view(), name='ingredients'),
    path('products/ingredients/create_ingredient', views.create_ingredient, name='create-ingredient'),
    path('products/ingredients/<int:ingredient_id>', views.edit_ingredient, name='edit-ingredient'),
]
