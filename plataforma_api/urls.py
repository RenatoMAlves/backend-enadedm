from django.contrib import admin
from django.urls import path, include
from plataforma_api import views

urlpatterns = [
  path('resultados', views.ResultList.as_view()),
  path('estados', views.EstadosList.as_view()),
  path('areas', views.AreaList.as_view()),
  path('cursos', views.CursosList.as_view()),
  path('resultados/<int:id_curso>', views.ResultByCursoList.as_view()),
  path('resultados/<slug:sigla>', views.ResultByEstadoList.as_view()),
  path('resultados/<int:id_curso>/<int:id_area>', views.ResultByCursoAndArea.as_view()),
]
