from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view),
    path('ors/', include('apps.ors.urls'))
]