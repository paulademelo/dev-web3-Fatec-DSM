from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('cadastro', views.cadastro),
    path('store', views.store),
    path('aluno', views.aluno)
]
