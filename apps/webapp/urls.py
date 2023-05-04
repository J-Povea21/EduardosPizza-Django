from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ors/', include('apps.ors.urls'))
]