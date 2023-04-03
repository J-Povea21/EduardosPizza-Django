from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.db_panel_view),
]