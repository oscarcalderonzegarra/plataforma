from django.shortcuts import render

def lista_vehiculos(request):
    return render(request, 'vehiculos/listar.html')

def seguimiento_portfolio(request):
    portfolio = {
        "T1": [
            {"nombre": "Bay Bridge", "status": "Listo", "semana": "Semana 1", "desviacion": "5 días", "entrega": "5 sept.", "prioridad": 4},
            {"nombre": "Mini-Mirja", "status": "En riesgo", "semana": "Semana 2", "desviacion": "3 días", "entrega": "1 sept.", "prioridad": 3},
        ],
        "T2": [
            {"nombre": "Moonshot", "status": "Estancado", "semana": "Semana 3", "desviacion": "2 días", "entrega": "3 sept.", "prioridad": 5},
            {"nombre": "Bigfish", "status": "Listo", "semana": "Semana 1", "desviacion": "1 día", "entrega": "2 sept.", "prioridad": 2},
        ]
    }
    return render(request, 'vehiculos/seguimiento.html', {'portfolio': portfolio})

def inicio(request):
    return render(request, 'vehiculos/inicio.html')

def agregar_vehiculo(request):
    return render(request, 'vehiculos/agregar.html')