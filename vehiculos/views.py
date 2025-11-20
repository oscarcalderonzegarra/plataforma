from django.shortcuts import render, redirect
from .models import Vehiculo #HAY QUE IMPORTAR LOS MODELOS PARA PODER USARLOS
from .forms import VehiculoForm
from django.shortcuts import render, redirect, get_object_or_404

def inicio(request):
    return render(request, 'vehiculos/inicio.html')


def lista_vehiculos(request): #REVISANDO Q ONDA
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/listar.html', {'vehiculos': vehiculos})

def seguimiento(request):
    return render(request, 'vehiculos/seguimiento.html')

def agregar_vehiculo(request):

    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculos:lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/agregar.html', {'form': form})
def detalle_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, pk=id)
    return render(request, 'vehiculos/detalle.html', {'vehiculo': vehiculo})

