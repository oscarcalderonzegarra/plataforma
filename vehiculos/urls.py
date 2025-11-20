from django.urls import path
from . import views

app_name = 'vehiculos'

urlpatterns = [
    path('', views.inicio, name='home'),
    path('agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('lista/', views.lista_vehiculos, name='lista_vehiculos'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('detalle/<int:id>/', views.detalle_vehiculo, name='detalle_vehiculo'),  # ← importante
]