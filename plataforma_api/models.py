from django.db import models

class Dim_ano(models.Model):
  ano = models.IntegerField()
  def __str__(self):
    return str(self.ano)

class Dim_regiao(models.Model):
  regiao = models.CharField(max_length=15)
  class Meta: 
    verbose_name_plural = "Dim_regioes"
  def __str__(self):
    return self.regiao

class Dim_estado(models.Model):
  estado = models.CharField(max_length=2)
  def __str__(self):
    return self.estado

class Dim_curso(models.Model):
  curso = models.CharField(max_length=50)
  def __str__(self):
    return self.curso

class Dim_area_enquadramento(models.Model):
  area = models.CharField(max_length=50)
  class Meta: 
    verbose_name_plural = "Dim_areas_enquadramento"
  def __str__(self):
    return self.area

class Ft_resultado(models.Model):
  volume_incidencias = models.IntegerField()
  volume_incidencias_porcentagem = models.IntegerField()
  porcentagem_certas = models.IntegerField()
  id_ano = models.ForeignKey(Dim_ano, related_name='id_ano', on_delete=models.PROTECT)
  id_regiao = models.ForeignKey(Dim_regiao, related_name='id_regiao', on_delete=models.PROTECT)
  id_estado = models.ForeignKey(Dim_estado, related_name='id_estado', on_delete=models.PROTECT)
  id_curso = models.ForeignKey(Dim_curso, related_name='id_curso', on_delete=models.PROTECT)
  id_area = models.ForeignKey(Dim_area_enquadramento, related_name='id_area', on_delete=models.PROTECT)
  def __str__(self):
    return "{} - {} ({})".format(self.id_ano, self.id_area, self.id_estado)
