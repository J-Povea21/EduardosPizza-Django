from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-order/', views.create_order, name='create-order'),
    path('order-detail/', views.order_detail, name='order-detail'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),
    path('rate-deliveryman', views.rate_deliveryman, name='rate-deliveryman'),
    path('ors/', include('apps.ors.urls'))
]