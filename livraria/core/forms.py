from django import forms
from core.models import Livro, Editora, Endereco, Autor


CATEGORIAS_LIVROS = [
    ('','Selecione'),
    ('Filosofia', 'Filosofia'),
    ('Religiao','Religiao'),
    ('Ciencia','Ciencia'),
    ('Romance','Romance'),
]

class DateInput(forms.DateInput):
    input_type = 'date'

class CheckboxInput(forms.CheckboxInput):
    input_type = 'checkbox'

class LivroForm(forms.ModelForm):
    ano = forms.DateField(widget=DateInput)

    list_editoras = Editora.objects.all().values()

    editora = forms.ChoiceField(choices=[('0','Selecione')]+ [(editora.id, editora.nome) for editora in  Editora.objects.all()])
    descricao = forms.CharField(widget=forms.Textarea())
    categorias = forms.ChoiceField(choices=CATEGORIAS_LIVROS)


   # categoria_nao_encontrada = forms.BooleanField(required=False, label='Não encontrei minha categoria')
    class Meta:
        model = Livro
        fields = ('nome', 'preco','estoque', 'edicao','num_paginas')

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