from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque', default=0)

    def __str__(self):
        return "'{}-{}-{}'".format(self.nome, self.preco, self.estoque)


class Livro(Produto):
    autor = models.CharField('Autor', max_length=100)
    edicao = models.IntegerField('Edicao', default=1)
    ano = models.DateField('Ano', blank=True)
    editora = models.ForeignKey('Editora', on_delete=models.CASCADE, related_name='editora')

    def __str__(self):
        return "'{}'-'{}'-'{} - {}'".format(self.autor, self.edicao, self.ano, self.editora.nome)


class Editora(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE, related_name='endereco')

    def __self__(self):
        return "'{} - {}'".format(self.nome, self.endereco)

class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=200)
    bairro = models.CharField('Bairro', max_length=200)
    cidade = models.CharField('Cidade', max_length=200)
    estado = models.CharField('Estado', max_length=200)
    numero = models.IntegerField('Numero', default=0)
    
    def __str__(self):
        return "'{}'-'{}'-'{} - {} - {}'".format(self.rua, self.bairro, self.cidade, self.estado,self.numero)
