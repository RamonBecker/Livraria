# Generated by Django 3.0.6 on 2020-05-28 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200525_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmprestimoLivro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial', models.DateTimeField(auto_now=True)),
                ('data_devolucao', models.DateField(blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preco')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livro', to='core.Livro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
