from django.shortcuts import render
from django.contrib.auth.models import User
from plataforma_api.serializers import ResultadoSerializer
from rest_framework import generics
from .models import Ft_resultado

class ResultList(generics.ListAPIView):
    queryset = Ft_resultado.objects.all()
    serializer_class = ResultadoSerializer