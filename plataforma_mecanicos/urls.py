"""
URL configuration for plataforma_mecanicos project.
"""

from django.contrib import admin
from django.urls import path
from vehiculos import views 

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('', views.inicio, name='inicio'),
]