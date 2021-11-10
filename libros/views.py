from copy import copy

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from libros.models import Libro
from libros.serializers import DetalleLibroSerializer, LibroSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class LibrosViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        data = copy(self.request.data)
        data['creado_por'] = self.request.user.id
        serializer_class = self.get_serializer_class()
        serialized = serializer_class(data=data)

        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )

        serialized.save()
        return Response(
            status=status.HTTP_201_CREATED,
            data=serialized.data
        )

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user:
                return self.queryset.filter(creado_por=self.request.user.id)

        try:
            data = {}
            for p in self.request.query_params:
                data[p] = self.request.query_params[p]
            return self.queryset.filter(**data)

        except:
            return self.queryset

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetalleLibroSerializer
        return self.serializer_class
