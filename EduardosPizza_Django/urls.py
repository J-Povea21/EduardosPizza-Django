"""
URL configuration for EduardosPizza_Django project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.webapp.urls')),
    path('ors/', include('apps.ors.urls')),
    path('admin/', admin.site.urls),
]
