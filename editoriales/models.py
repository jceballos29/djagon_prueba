from django.db import models

# Create your models here.


class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    cantidad_publicaciones = models.IntegerField()
    direccion = models.CharField(max_length=500, default='')


    def __str__(self) -> str:
        return self.nombre