from django.contrib import admin
from django.urls import path, include
from plataforma_api import views

urlpatterns = [
  path('resultados', views.ResultList.as_view()),
  path('estados', views.EstadosList.as_view()),
  path('areas', views.AreaList.as_view()),
  path('cursos', views.CursosList.as_view()),
]
