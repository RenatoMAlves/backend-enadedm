from .models import Ft_resultado, Dim_estado, Dim_area_enquadramento, Dim_curso
from rest_framework import serializers 

class ResultadoSerializer(serializers.Serializer):
  id_ano = serializers.SlugRelatedField(slug_field = 'ano', read_only=True)
  id_area = serializers.SlugRelatedField(slug_field = 'area', read_only=True)
  id_curso = serializers.SlugRelatedField(slug_field = 'curso', read_only=True)
  id_regiao = serializers.SlugRelatedField(slug_field = 'regiao', read_only=True)
  id_estado = serializers.SlugRelatedField(slug_field = 'sigla', read_only=True)
  volume_incidencias = serializers.IntegerField()
  volume_incidencias_porcentagem = serializers.FloatField()
  porcentagem_certas = serializers.FloatField()
  class Meta:
    model = Ft_resultado
    fields = ('id_estado', 'volume_incidencias', 'volume_incidencias_porcentagem', 'porcentagem_certas')
  
class EstadoSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  sigla = serializers.CharField()
  class Meta:
    model = Dim_estado
    fields = ('id', 'sigla')

class AreaSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  area = serializers.CharField()
  class Meta:
    model = Dim_area_enquadramento
    fields = ('id', 'area')
    
class CursoSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  curso = serializers.CharField()
  class Meta:
    model = Dim_estado
    fields = ('id', 'curso')