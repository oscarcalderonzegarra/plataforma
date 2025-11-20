from django.urls import path
from . import views

app_name = 'vehiculos'

urlpatterns = [
    path('', views.inicio, name='inicio'), #REVISANDO ESTO
    path('listar/', views.lista_vehiculos, name='lista_vehiculos'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
]