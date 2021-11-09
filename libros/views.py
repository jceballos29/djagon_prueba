# from django.shortcuts import render

# # Create your views here.
# from libros.models import Libro
# from libros.serializers import LibroSerializer

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(http_method_names=['GET', 'POST'])
# def libros(request):
#     if request.method == 'GET':
#         libros = Libro.objects.all()
#         librosSerializer = LibroSerializer(libros, many=True)
#         return Response(data = {'libros': librosSerializer.data})

#     if request.method == 'POST':
#         libro = LibroSerializer(data=request.data)
#         if libro.is_valid():
#             libro.save()
#             return Response(libro.data, status=status.HTTP_201_CREATED)
#         return Response(libro.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=['GET', 'PUT', 'DELETE'])
# def libro(request, id):
#     try: 
#         libro = Libro.objects.get(id=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         libroSerializer = LibroSerializer(libro)
#         return Response(libroSerializer.data)

#     if request.method == 'DELETE':
#         libro.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     if request.method == 'PUT':
#         libroSerializer = LibroSerializer(libro, request.data)
#         if libroSerializer.is_valid():
#             libroSerializer.save()
#             return Response(libroSerializer.data)
#         return Response(libro.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from libros.models import Libro
from libros.serializers import DetalleLibroSerializer, LibroSerializer

class LibrosViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_serializer_class(self):
        print(self.request.method)
        print(self.action)
        print(self.request.user.email)
        print(self.request.user.is_staff)
        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetalleLibroSerializer
        return self.serializer_class