from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin

#Cadastros


from .views import base, cadastrarProduto, cadastrarEditora
from .views import exibir_livros, detalhe_livro , editar_livro

urlpatterns = [
    path('', base, name='base'),
    #Cadastros
    
    path('cadastrarProduto/', cadastrarProduto, name='cadastrarProduto'),
    path('cadastrarEditora/', cadastrarEditora, name='cadastrarEditora'),

    #Exibição de produtos cadastrados
    path('exibirLivros/', exibir_livros,name='exibirLivros'),

    #Detalhes do produto
    path('detalheLivro/<int:pk>', detalhe_livro,name='detalheLivro'),

    #Editar produto
    path('editarLivro/<int:pk>',editar_livro, name='editarLivro')
    
]
