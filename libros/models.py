from django.contrib.auth.models import User
from django.db import models
from autores.models import Autor

from editoriales.models import Editorial


class Libro(models.Model):
    nombre = models.CharField(max_length=300)
    paginas = models.IntegerField()
    publicado = models.BooleanField()
    fecha_publicacion = models.DateField()
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.SET_NULL,
        null=True,
        related_name='libros'
    )

    autores = models.ManyToManyField(Autor, related_name='libros')
    editores = models.ManyToManyField(Autor, through='EditoresLibro')
    creado_por = models.ForeignKey(User, related_name='lilbros_creados', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nombre


class EditoresLibro(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
