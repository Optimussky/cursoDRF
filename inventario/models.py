from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name = "Descripción")
    marca = models.CharField(max_length=50)
    cantidad_min = models.IntegerField()
    cantidad_max = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre
