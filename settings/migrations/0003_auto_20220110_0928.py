# Generated by Django 3.2.8 on 2022-01-10 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0024_alter_produtocliente_file'),
        ('settings', '0002_rename_configuracoes_configuracoesproduto'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracoesproduto',
            name='categoriaProduto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='produtos.categoriaproduto', verbose_name='Categoria de produto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracoesproduto',
            name='classeProduto',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='produtos.classeproduto', verbose_name='Classe de produto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracoesproduto',
            name='segmento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produtos.segmento', verbose_name='segmento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracoesproduto',
            name='tipoProduto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produtos.tipoproduto', verbose_name='tipo de produto'),
            preserve_default=False,
        ),
    ]
