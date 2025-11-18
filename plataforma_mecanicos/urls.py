# plataforma_mecanicos/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehiculos.urls', namespace='vehiculos')),  # ← esto activa el namespace
]