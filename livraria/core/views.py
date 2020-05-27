from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

from .forms import LivroForm, EditoraForm, EnderecoForm, AutorForm
from .models import Editora, Endereco, Autor, Livro, Categoria


@login_required
def base(request):
    return render(request, 'base.html')


# Funções para realizar cadastros
@login_required
def cadastrarProduto(request):
    print(request.POST.get('vehicle1'))
    form_Livro = LivroForm(request.POST or None)
    form_Autor = AutorForm(request.POST or None)
  #  formEditora = EditoraForm(request.POST or None)
    
    if str(request.method) == 'POST':
        if form_Livro.is_valid():
            if form_Autor.is_valid():
                print(form_Livro.cleaned_data)
                print(form_Autor.cleaned_data)
                #Pegando dados do formulário de Livro
                
                nomeLivro = form_Livro.cleaned_data['nome']
                print(nomeLivro)
                preco = form_Livro.cleaned_data['preco']
                estoque = form_Livro.cleaned_data['estoque']
                edicao = form_Livro.cleaned_data['edicao']
                nome_categoria = form_Livro.cleaned_data['categorias']
                num_paginas = form_Livro.cleaned_data['num_paginas']
                descricao = form_Livro.cleaned_data['descricao']
                anoLivro = form_Livro.cleaned_data['ano']
            
                #Buscando editora selecionada

                #print(form_Livro.cleaned_data['descricao'])

                idEditora = form_Livro.cleaned_data['editora']
                editora = Editora.objects.get(id=idEditora)

                #Pegando dados do formulario do autor
                nomeAutor = form_Autor.cleaned_data['nomeAutor']
                data_nascimento = form_Autor.cleaned_data['ano']
                
                #Pegando categoria do bd, se não encontrar cria uma nova categoria

                categoria,created =  Categoria.objects.get_or_create(nome=nome_categoria)              

                #Pegando autor do bd, se não encontrar cria um autor
                autor,created = Autor.objects.get_or_create(nome=nomeAutor, data_nascimento=data_nascimento)

                #Pega o livro do bd, se não encontrar cria um livro novo
                livro, created = Livro.objects.get_or_create(nome=nomeLivro,preco=preco,estoque=estoque,edicao=edicao,num_paginas=num_paginas,descricao=descricao, ano=anoLivro, autor=autor,editora=editora, categoria=categoria)
                livro.preco_total = estoque * preco
                livro.save()
                #messages.success(request,'Livro cadastrado com sucesso !')
            

    #form_Livro = LivroForm()
    #form_Autor = AutorForm()
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
def exibir_livros(request):

    list_Livros = Livro.objects.all().values()

    list_preco_total = []
    context= {
        'livros': Livro.objects.all(),
        'livros_preco_total':list_preco_total
    }

    return render(request,'produto/exibir_produtos.html',context)


@login_required
def detalhe_livro(request, pk):

    livro = get_object_or_404(Livro,id=pk)

    context = {
        'livro':livro,
    }

    return render(request,'produto/detalhe_produto.html', context)

@login_required
def editar_livro(request,pk):

    livro = get_object_or_404(Livro, pk=pk)
    
    formLivro = LivroForm(request.POST or None)
    formAutor = AutorForm(request.POST or None)

    if str(request.method) == 'POST':
        formLivro = LivroForm(request.POST, instance=livro)
        if formLivro.is_valid():
            if formAutor.is_valid():
                #livro = formLivro.save(commit=False)
 
                livro = formLivro.save(commit=False)
                livro.nome = formLivro.cleaned_data['nome']
                livro.preco = formLivro.cleaned_data['preco']
                livro.estoque = formLivro.cleaned_data['estoque']
                livro.num_paginas = formLivro.cleaned_data['num_paginas']
                livro.edicao = formLivro.cleaned_data['edicao']
                livro.descricao = formLivro.cleaned_data['descricao']
                livro.ano = formLivro.cleaned_data['ano']

                nomeAutor = formAutor.cleaned_data['nomeAutor']
                data_nascimento = formAutor.cleaned_data['ano']

                nomeCategoria = formLivro.cleaned_data['categorias']

                autor,created = Autor.objects.get_or_create(nome=nomeAutor, data_nascimento=data_nascimento)
                categoria, created = Categoria.objects.get_or_create(nome=nomeCategoria)
                
                livro.autor = autor
                livro.categoria = categoria
                livro.save()
                
                return redirect('exibirLivros')
    else:
        formLivro = LivroForm(instance=livro) 
        formAutor = AutorForm()

    context = {
        'formLivro':formLivro,
        'formAutor': formAutor,
    }

    return render(request,'forms/editar_produto.html',context)


@login_required
def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    livro.delete()
    return redirect('exibirLivros')
