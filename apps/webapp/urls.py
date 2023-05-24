from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_order/', views.create_order, name='create_order'),
    path('ors/', include('apps.ors.urls'))
]