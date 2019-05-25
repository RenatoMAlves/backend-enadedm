from django.db import models

class Dim_ano(models.Model):
  ano = models.IntegerField(primary_key=True)
  def __str__(self):
    return str(self.ano)

class Dim_regiao(models.Model):
  id = models.IntegerField(primary_key=True)
  regiao = models.CharField(max_length=15)
  class Meta: 
    verbose_name_plural = "Dim_regioes"
  def __str__(self):
    return self.regiao

class Dim_curso(models.Model):
  id = models.IntegerField(primary_key=True)
  curso = models.CharField(max_length=50)
  def __str__(self):
    return "{} - {}".format(self.id,self.curso)

class Dim_area_enquadramento(models.Model):
  id = models.IntegerField(primary_key=True)
  area = models.CharField(max_length=50)
  class Meta: 
    verbose_name_plural = "Dim_areas_enquadramento"
  def __str__(self):
    return "{} - {}".format(self.id,self.area)

class Ft_resultado(models.Model):
  volume_incidencias = models.IntegerField(default=0)
  porcentagem_incidencias = models.FloatField(default=0)
  qtd_questoes = models.IntegerField(default=0)
  qtd_certas = models.IntegerField(default=0)
  qtd_erradas = models.IntegerField(default=0)
  qtd_branco_invalidas = models.IntegerField(default=0)
  porcentagem_certas = models.FloatField(default=0)
  porcentagem_erradas = models.FloatField(default=0)
  porcentagem_branco_invalida = models.FloatField(default=0)
  ano = models.ForeignKey(Dim_ano, related_name='id_ano', on_delete=models.PROTECT)
  id_regiao = models.ForeignKey(Dim_regiao, related_name='id_regiao', on_delete=models.PROTECT)
  id_curso = models.ForeignKey(Dim_curso, related_name='id_curso', on_delete=models.PROTECT)
  id_area = models.ForeignKey(Dim_area_enquadramento, related_name='id_area', on_delete=models.PROTECT)

  def __str__(self):
    return "{} - {} ({})".format(self.ano, self.id_area, self.id_regiao)


class Ft_associacao(models.Model):
  antecedente = models.CharField(max_length=100)
  consequente = models.CharField(max_length=50)
  total = models.IntegerField(default=0)
  ano = models.ForeignKey(Dim_ano, related_name='id_ano_id', on_delete=models.PROTECT)
  id_curso = models.ForeignKey(Dim_curso, related_name='id_curso_id', on_delete=models.PROTECT)

  def __str__(self):
    return "{}".format(self.ano)
