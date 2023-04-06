from django.urls import path, include
from . import views

urlpatterns = [
    path('create_order', views.create_order, name='create_order'),
]
