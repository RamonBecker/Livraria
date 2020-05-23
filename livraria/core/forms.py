from django import forms
from core.models import Livro, Editora, Endereco, Autor


class DateInput(forms.DateInput):
    input_type = 'date'

class LivroForm(forms.ModelForm):
    ano = forms.DateField(widget=DateInput)
    editora = forms.ChoiceField(choices=[('0','Selecione')]+ [(editora.id, editora.nome) for editora in  Editora.objects.all()])
    descricao = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Livro
        fields = ('nome', 'preco', 'estoque','edicao','num_paginas')

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ('nome',)

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('rua','bairro','cidade','estado','numero')

class AutorForm(forms.ModelForm):
    ano = forms.DateField(widget=DateInput)
    class Meta:
        model = Autor
        fields = ('nome',)