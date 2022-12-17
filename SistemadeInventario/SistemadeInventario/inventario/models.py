from django.db import models

# Base de datos

class Inventario(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    medida = models.CharField(max_length=3, null=False, blank=False)

# Parámetros dentro de () indican requerimientos/reglas.

def __str__(self) -> str:
    return self.name # Devuelve el nombre del producto en la página Web