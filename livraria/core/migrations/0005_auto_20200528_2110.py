# Generated by Django 3.0.6 on 2020-05-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200528_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimolivro',
            name='data_inicial',
            field=models.DateTimeField(blank=True),
        ),
    ]
