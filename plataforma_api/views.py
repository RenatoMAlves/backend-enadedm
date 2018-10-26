from django.shortcuts import render
from django.contrib.auth.models import User
from plataforma_api.serializers import *
from rest_framework import generics
from .models import Ft_resultado, Dim_estado, Dim_area_enquadramento, Dim_curso

class ResultList(generics.ListAPIView):
    queryset = Ft_resultado.objects.all()
    serializer_class = ResultadoSerializer

class ResultByCursoList(generics.ListAPIView):
    serializer_class = ResultadoSerializer
    def get_queryset(self):
        curso = self.kwargs['id_curso']
        return Ft_resultado.objects.filter(id_curso = curso)

class ResultByEstadoList(generics.ListAPIView):
    serializer_class = ResultadoSerializer
    def get_queryset(self):
        sigla = self.kwargs['sigla']
        return Ft_resultado.objects.filter(id_estado__sigla = sigla)

class ResultByCursoAndArea(generics.ListAPIView):
    serializer_class = ResultadoSerializer
    def get_queryset(self):
        curso = self.kwargs['id_curso']
        area = self.kwargs['id_area']
        return Ft_resultado.objects.filter(id_curso = curso).filter(id_area = area)

class EstadosList(generics.ListAPIView):
    queryset = Dim_estado.objects.all()
    serializer_class = EstadoSerializer

class AreaList(generics.ListAPIView):
    queryset = Dim_area_enquadramento.objects.all()
    serializer_class = AreaSerializer

class CursosList(generics.ListAPIView):
    queryset = Dim_curso.objects.all()
    serializer_class = CursoSerializer