from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin

#Cadastros
from .views import base, cadastrarProduto, cadastrarEditora, exibir_produtos

urlpatterns = [
    path('', base, name='base'),
    #Cadastros
    path('cadastrarProduto/', cadastrarProduto, name='cadastrarProduto'),
    path('cadastrarEditora/', cadastrarEditora, name='cadastrarEditora'),

    #Exibição de produtos
    path('exibirProdutos/', exibir_produtos,name='exibirProdutos'),
]
