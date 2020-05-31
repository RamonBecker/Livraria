from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin


#View
from .views import base, cadastrarProduto, cadastrarEditora
from .views import exibir_livros, detalhe_livro , editar_livro, deletar_livro
from .views import realizar_emprestimo,devolver_livro

urlpatterns = [
    path('', base, name='base'),
    #Cadastros
    
    path('cadastrarProduto/', cadastrarProduto, name='cadastrarProduto'),
    path('cadastrarEditora/', cadastrarEditora, name='cadastrarEditora'),

    #Exibição de livros cadastrados
    path('exibirLivros/', exibir_livros,name='exibirLivros'),

    #Detalhes do livros
    path('detalheLivro/<int:pk>', detalhe_livro,name='detalheLivro'),

    #Editar livors
    path('editarLivro/<int:pk>',editar_livro, name='editarLivro'),

    #Deletar livro
    path('deletarLivro/<int:pk>', deletar_livro, name='deletarLivro'),

    #Realizar emprestimo
    path('emprestimoLivro/<int:pk>', realizar_emprestimo, name='emprestimoLivro'),

    #Devolver Livro
    path('devolverLivro/<int:pk>',devolver_livro, name='devolverLivro')

]
