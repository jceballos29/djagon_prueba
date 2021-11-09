from django.db import models
from django.shortcuts import render
# Create your views here.
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# class EditorialesGenericView(ListCreateAPIView):
#     queryset = Editorial.objects.all()
#     serializer_class = EditorialSerializer

# class EditorialDetailGenericView(RetrieveUpdateDestroyAPIView):
#     queryset = Editorial.objects.all()
#     serializer_class = EditorialSerializer

class EditorialViewSet(ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer