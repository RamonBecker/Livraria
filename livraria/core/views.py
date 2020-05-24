from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from .forms import LivroForm, EditoraForm, EnderecoForm, AutorForm
from .models import Editora, Endereco, Autor, Livro

@login_required
def base(request):
    return render(request, 'base.html')


# Funções para realizar cadastros
@login_required
def cadastrarProduto(request):

    form_Livro = LivroForm(request.POST or None)
    form_Autor = AutorForm(request.POST or None)
  #  formEditora = EditoraForm(request.POST or None)
 
    if str(request.method) == 'POST':
        if form_Livro.is_valid():
            if form_Autor.is_valid():
                #Pegando dados do formulário de Livro
                
                nomeLivro = form_Livro.cleaned_data['nome']
                preco = form_Livro.cleaned_data['preco']
                estoque = form_Livro.cleaned_data['estoque']
                edicao = form_Livro.cleaned_data['edicao']
                genero = form_Livro.cleaned_data['genero']
                num_paginas = form_Livro.cleaned_data['num_paginas']
                descricao = form_Livro.cleaned_data['descricao']
                anoLivro = form_Livro.cleaned_data['ano']
            
                #Buscando editora selecionada

                #print(form_Livro.cleaned_data['descricao'])

                idEditora = form_Livro.cleaned_data['editora']
                editora = Editora.objects.get(id=idEditora)

                #Pegando dados do formulario do autor
                nomeAutor = form_Autor.cleaned_data['nome']
                data_nascimento = form_Autor.cleaned_data['ano']

                #Pegando autor do bd, se não encontrar cria um autor
                autor,created = Autor.objects.get_or_create(nome=nomeAutor, data_nascimento=data_nascimento)

                #Pega o livro do bd, se não encontrar cria um livro novo
                livro, created = Livro.objects.get_or_create(nome=nomeLivro,preco=preco,estoque=estoque,edicao=edicao,genero=genero,num_paginas=num_paginas,descricao=descricao, ano=anoLivro, autor=autor,editora=editora)
  

                livro.save()
                messages.success(request,'Livro cadastrado com sucesso !')


    form_Livro = LivroForm()
    form_Autor = AutorForm()
    context = {
        'formLivro': form_Livro,
        'formAutor': form_Autor
    }
    

    return render(request, 'forms/add_livro.html', context)

@login_required
def cadastrarEditora(request):

    aux_Editora_form = EditoraForm(request.POST or None)
    aux_Endereco_form = EnderecoForm(request.POST or None)

    invalid_Form = False

    if str(request.method) == 'POST':
        if aux_Editora_form.is_valid():
            if aux_Endereco_form.is_valid():

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
                messages.success(request,'Editora cadastrada com sucesso !')
            else:
                invalid_Form = True
        else:
            invalid_Form = True
    else:
        invalid_Form = True

    if invalid_Form :
        messages.error(request,'Erro ao cadastrar editora !')

                
    aux_Editora_form = EditoraForm()
    aux_Endereco_form = EnderecoForm()

    context = {
         'editoraForm':aux_Editora_form,
         'enderecoForm': aux_Endereco_form,
    }

    return render(request, 'forms/add_editora.html', context)


# Mostrar listagem de objetos
@login_required
def exibir_produtos(request):
    return render(request,'my_products.html')