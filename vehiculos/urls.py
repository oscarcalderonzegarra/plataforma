from django.urls import path
from vehiculos import views

urlpatterns = [
    path('', views.lista_vehiculos, name='lista_vehiculos'),
]