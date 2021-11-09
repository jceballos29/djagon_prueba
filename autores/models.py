from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=120)
    nacionalidad = models.CharField(max_length=100, default='')
    fecha_nacimeinto = models.DateField()


    def __str__(self) -> str:
        return self.nombre