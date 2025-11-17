from django.db import models

# Create your models here.
from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    patente = models.CharField(max_length=10, unique=True)
    en_reparacion = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"