from django import forms
from core.models import Livro, Editora, Endereco


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('nome', 'preco', 'estoque', 'autor', 'edicao', 'ano','editora')

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ('nome',)

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('rua','bairro','cidade','estado','numero')