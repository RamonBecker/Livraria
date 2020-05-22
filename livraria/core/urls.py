from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin

#Cadastros
from .views import base, cadastrarProduto, cadastrarEditora

urlpatterns = [
    path('', base, name='base'),
    #Cadastros
    path('cadastrarProduto/', cadastrarProduto, name='cadastrarProduto'),
    path('cadastrarEditora/', cadastrarEditora, name='cadastrarEditora'),
]
