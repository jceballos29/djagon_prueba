from copy import copy

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from autores.serializers import AutorSerializer
from libros.models import Libro
from libros.serializers import DetalleLibroSerializer, LibroSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
# from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action


class LibrosViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = (AllowAny,)
    # pagination_class = LimitOffsetPagination

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
                if p in ['page',  'order_by', ]:
                    continue
                data[p] = self.request.query_params[p]
            return self.queryset.filter(**data)

        except Exception as e:
            print(e)
            return self.queryset

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetalleLibroSerializer
        return self.serializer_class

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def autores(self, request, pk=None):
        libro = self.get_object()

        if request.method == 'GET':
            autores = libro.autores.all()
            serialized = AutorSerializer(autores, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

        if request.method == 'POST':
            autores_nuevos = request.data["autores_id"]
            print(autores_nuevos)

            libro.autores.add(*autores_nuevos)
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            eliminar_autores = request.data['autores_id']
            libro.autores.remove(*eliminar_autores)
            return Response(status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def publicar(self, request, pk=None):
        libro = Libro.objects.get(id=pk)
        libro.publicado = True
        libro.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def order(self, request):
        order_by = '-id'
        if 'order_by' in self.request.query_params:
            order_by = self.request.query_params['order_by']
        queryset = self.get_queryset().order_by(order_by)
        serializer_class = self.get_serializer_class()
        serialized = serializer_class(queryset, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    @action(methods=['POST'], detail=False)
    def reset(self, request):
        queryset = self.get_queryset()
        for libro in queryset:
            libro.publicado = False
            libro.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def reset_authors(self, request):
        queryset = self.get_queryset()
        for libro in queryset:
            libro.autores.set([])
            libro.save()
        return Response(status=status.HTTP_200_OK)