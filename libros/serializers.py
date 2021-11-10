from rest_framework.serializers import ModelSerializer

from autores.serializers import AutorSerializer
from libros.models import Libro


class LibroSerializer(ModelSerializer):
    # autores = AutorSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = '__all__'


class CrearLibrosSerializer(ModelSerializer):

    class Meta:
        model = Libro
        fields = '__all__'


class DetalleLibroSerializer(ModelSerializer):

    class Meta:
        model= Libro
        fields = '__all__'