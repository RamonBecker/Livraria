from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from .forms import LivroForm, EditoraForm, EnderecoForm
from .models import Editora, Endereco

@login_required
def base(request):
    return render(request, 'base.html')


# Funções para realizar cadastros
@login_required
def cadastrarProduto(request):
    form = LivroForm(request.POST or None)
    formEditora = EditoraForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            if formEditora.is_valid():
               pass  
        
    context = {
        'form': form,
        'editoras': Editora.objects.all()
    }

    print(len(context.get('editoras')) == 0)
    return render(request, 'forms/add_livro.html', context)

@login_required
def cadastrarEditora(request):
    aux_Editora_form = EditoraForm(request.POST or None)
    aux_Endereco_form = EnderecoForm(request.POST or None)

    if str(request.method) == 'POST':
        if aux_Editora_form.is_valid():
            if aux_Endereco_form.is_valid():
                '''
                editora = aux_Editora_form.save(commit=false)
                editora.endereco = aux_Endereco_form.save()
                aux_Editora_form.save()    
                messages.success(request, 'Produto salvo com sucesso')
                aux_Endereco_form = EnderecoForm()
                aux_Editora_form = EditoraForm()
                '''
               # aux_Editora_form.cleaned_data
                #aux_Endereco_form.cleaned_data
              #  print(aux_Editora_form.cleaned_data)
                print(aux_Endereco_form.cleaned_data)

                rua = aux_Endereco_form.cleaned_data['rua']
                bairro = aux_Endereco_form.cleaned_data['bairro']
                cidade = aux_Endereco_form.cleaned_data['cidade']
                estado = aux_Endereco_form.cleaned_data['estado']
                numero = aux_Endereco_form.cleaned_data['numero']
                nomeEditora = aux_Editora_form.cleaned_data['nome']

                endereco,created = Endereco.objects.get_or_create(rua=rua, bairro=bairro, cidade=cidade, estado=estado, numero=numero)
                editora, created = Editora.objects.get_or_create(nome=nomeEditora, endereco=endereco)
                editora.save()
                print('Endereço:',endereco)
                print('Editora:', editora)
                
                aux_Editora_form = EditoraForm()
                aux_Endereco_form = EnderecoForm()
                
    context = {
         'editoraForm':aux_Editora_form,
         'enderecoForm': aux_Endereco_form,
    }

    return render(request, 'forms/add_editora.html', context)
