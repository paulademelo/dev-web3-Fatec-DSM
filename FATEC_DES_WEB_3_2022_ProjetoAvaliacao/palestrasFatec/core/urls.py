from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cadastrar', views.cadastrar),
    path('alunos', views.alunos_cadastrados)
    ]