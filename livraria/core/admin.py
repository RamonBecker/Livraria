from django.contrib import admin

from .models import Editora, Endereco, Autor, Livro, Categoria

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome','data_nascimento')

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua','bairro','cidade','numero','estado')

@admin.register(Livro)
class Livro(admin.ModelAdmin):
    list_display = ('nome','preco','estoque','autor','editora','descricao','num_paginas','ano','edicao', 'categoria')
