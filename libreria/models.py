from django.db import models

# Create your models here.

class Editorial(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.PROTECT,
        related_name='libros'
    )
    nombre = models.CharField(max_length=200)
    precio = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

