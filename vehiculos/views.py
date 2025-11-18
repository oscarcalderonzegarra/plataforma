from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/lista.html', {'vehiculos': vehiculos})

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/agregar.html', {'form': form})