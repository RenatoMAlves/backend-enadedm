from django.shortcuts import render
from django.contrib.auth.models import User
from plataforma_api.serializers import *
from rest_framework import generics
from .models import Ft_resultado, Dim_estado, Dim_area_enquadramento, Dim_curso

class ResultList(generics.ListAPIView):
    queryset = Ft_resultado.objects.all()
    serializer_class = ResultadoSerializer

class EstadosList(generics.ListAPIView):
    queryset = Dim_estado.objects.all()
    serializer_class = EstadoSerializer

class AreaList(generics.ListAPIView):
    queryset = Dim_area_enquadramento.objects.all()
    serializer_class = AreaSerializer

class CursosList(generics.ListAPIView):
    queryset = Dim_curso.objects.all()
    serializer_class = CursoSerializer