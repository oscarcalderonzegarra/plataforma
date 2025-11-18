from django.db import models

class Mecanico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    ESTADOS = [
        ('espera', 'En espera'),
        ('reparacion', 'En reparación'),
        ('listo', 'Listo para entrega'),
    ]

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    patente = models.CharField(max_length=10, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='espera')
    mecanico = models.ForeignKey(Mecanico, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"