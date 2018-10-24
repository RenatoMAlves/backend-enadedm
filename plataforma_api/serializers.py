from .models import Ft_resultado
from rest_framework import serializers

class ResultadoSerializer(serializers.Serializer):
  id_ano = serializers.SlugRelatedField(slug_field = 'ano', read_only=True)
  id_area = serializers.SlugRelatedField(slug_field = 'area', read_only=True)
  id_curso = serializers.SlugRelatedField(slug_field = 'curso', read_only=True)
  id_regiao = serializers.SlugRelatedField(slug_field = 'regiao', read_only=True)
  id_estado = serializers.SlugRelatedField(slug_field = 'estado', read_only=True)
  volume_incidencias = serializers.IntegerField()
  volume_incidencias_porcentagem = serializers.IntegerField()
  porcentagem_certas = serializers.IntegerField()
  class Meta:
    model = Ft_resultado
    fields = ('ano', 'area', 'curso', 'regiao', 'estado', 'volume_incidencias', 'volume_incidencias_porcentagem', 'porcentagem_certas')
    