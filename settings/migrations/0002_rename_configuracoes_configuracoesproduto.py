# Generated by Django 3.2.8 on 2021-12-28 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0023_auto_20211227_1146'),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Configuracoes',
            new_name='ConfiguracoesProduto',
        ),
    ]
