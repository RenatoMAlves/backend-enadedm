from .models import Ft_resultado, Dim_area_enquadramento, Dim_curso, Dim_regiao, Dim_ano
from rest_framework import serializers 

class ResultadoSerializer(serializers.Serializer):
  ano = serializers.SlugRelatedField(slug_field = 'ano', read_only=True)
  id_area = serializers.SlugRelatedField(slug_field = 'area', read_only=True)
  id_curso = serializers.SlugRelatedField(slug_field = 'curso', read_only=True)
  id_regiao = serializers.SlugRelatedField(slug_field = 'regiao', read_only=True)
  volume_incidencias = serializers.IntegerField()
  porcentagem_incidencias = serializers.FloatField()
  qtd_questoes = serializers.IntegerField()
  qtd_certas = serializers.IntegerField()
  qtd_erradas = serializers.IntegerField()
  qtd_branco_invalidas = serializers.IntegerField()
  porcentagem_certas = serializers.FloatField()
  porcentagem_erradas = serializers.FloatField()
  porcentagem_branco_invalida = serializers.FloatField()
  class Meta:
    model = Ft_resultado
    fields = ('volume_incidencias', 'volume_incidencias_porcentagem', 'porcentagem_certas')

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
    model = Dim_curso
    fields = ('id', 'curso')

class RegiaoSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  regiao = serializers.CharField()
  class Meta:
    model = Dim_regiao
    fields = ('id', 'regiao')

class AnoSerializer(serializers.Serializer):
  ano = serializers.IntegerField()
  class Meta:
    model = Dim_ano
    fields = ('ano')