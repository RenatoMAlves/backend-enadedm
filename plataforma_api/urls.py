from django.contrib import admin
from django.urls import path, include
from plataforma_api import views

urlpatterns = [
  path('resultados', views.ResultList.as_view()),
  path('areas', views.AreaList.as_view()),
  path('cursos', views.CursosList.as_view()),
  path('regioes', views.RegioesList.as_view()),
  path('anos', views.AnoList.as_view()),
  path('resultados/<int:id_curso>', views.ResultByCursoList.as_view()),
  # path('resultados/<int:id_curso>/<int:id_area>', views.ResultByCursoAndArea.as_view()),
  path('resultados/<int:ano>/<int:id_curso>', views.ResultByAnoAndCurso.as_view()),
  path('resultados/<int:ano>/<int:curso>/<int:area>', views.ResultByAnoCursoAndArea.as_view()),
  path('ft-resultados/<int:ano>/<int:id_curso>', views.Ft_associacaoList.as_view()),
]