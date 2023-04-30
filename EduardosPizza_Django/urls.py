"""
URL configuration for EduardosPizza_Django project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('apps.webapp.urls', 'webapp'))),
    path('ors/', include(('apps.ors.urls', 'ors'))),
    path('admin/', admin.site.urls),
]
