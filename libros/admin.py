from django.contrib import admin


# Register your models here.

from libros.models import EditoresLibro, Libro


admin.site.register(Libro)

admin.site.register(EditoresLibro)

