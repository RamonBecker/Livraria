# Generated by Django 3.0.6 on 2020-05-20 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200519_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200, verbose_name='Rua')),
                ('bairro', models.CharField(max_length=200, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=200, verbose_name='Estado')),
                ('numero', models.IntegerField(default=0, verbose_name='Numero')),
            ],
        ),
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(default=0, verbose_name='Estoque'),
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('produto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Produto')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('edicao', models.IntegerField(default=1, verbose_name='Edicao')),
                ('ano', models.DateField(blank=True, verbose_name='Ano')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editora', to='core.Editora')),
            ],
            bases=('core.produto',),
        ),
        migrations.AddField(
            model_name='editora',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='core.Endereco'),
        ),
    ]