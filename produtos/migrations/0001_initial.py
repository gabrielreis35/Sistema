# Generated by Django 3.2.8 on 2021-11-24 10:46

from django.db import migrations, models
import django.db.models.deletion
import produtos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colaborator', '0001_initial'),
        ('workOrder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10, unique=True)),
                ('sigla', models.CharField(max_length=5, unique=True)),
                ('dateCriacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClasseProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10, unique=True)),
                ('sigla', models.CharField(max_length=3, unique=True)),
                ('dateCriacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, unique=True)),
                ('sigla', models.CharField(max_length=20, unique=True)),
                ('dateCriacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True)),
                ('sigla', models.CharField(max_length=3, unique=True)),
                ('dateCriacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('equipamento', models.CharField(max_length=10)),
                ('capacidade', models.FloatField()),
                ('largura', models.IntegerField()),
                ('espessura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('descontinuado', models.BooleanField()),
                ('dateCriacao', models.DateTimeField(auto_now_add=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.categoriaproduto')),
                ('classeAplicacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.classeproduto')),
                ('responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='colaborator.colaborador')),
                ('segmento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.segmento')),
                ('tipoProduto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.tipoproduto')),
            ],
        ),
        migrations.CreateModel(
            name='NumeroSerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(max_length=15, unique=True)),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workOrder.ordemservico')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revisao', models.IntegerField()),
                ('nome', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=8)),
                ('partNumber', models.CharField(max_length=16, null=True)),
                ('tipoFabricacao', models.CharField(choices=[('Montagem Geral', 'Montagem Geral'), ('Montagem', 'Montagem'), ('Usinagem', 'Usinagem'), ('Soldado', 'Conjunto Soldado'), ('CNC', 'Corte CNC'), ('CNC / Dobra', 'Corte CNC com Dobra'), ('CNC / Usinagem', 'Corte CNC com Usinagem'), ('CNC / Dobra / Usinagem', 'Corte CNC com Dobra e Usinagem'), ('Manual', 'Corte Manual'), ('Manual / Dobra', 'Corte Manual com Dobra'), ('Manual / Usinagem', 'Corte Manual com Usinagem'), ('Manual / Dobra / Usinagem', 'Corte Manual com Dobra e Usinagem')], max_length=25)),
                ('file', models.FileField(upload_to=produtos.models.Item.filePath)),
                ('dateCriacao', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revisao', models.IntegerField()),
                ('nome', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('DWG', 'DWG'), ('DXF', 'DXF'), ('eDRA', 'eDrawing'), ('PDF', 'PDF')], max_length=4)),
                ('partNumber', models.CharField(max_length=16, null=True)),
                ('tipoFabricacao', models.CharField(choices=[('Montagem Geral', 'Montagem Geral'), ('Montagem', 'Montagem'), ('Usinagem', 'Usinagem'), ('Soldado', 'Conjunto Soldado'), ('CNC', 'Corte CNC'), ('CNC / Dobra', 'Corte CNC com Dobra'), ('CNC / Usinagem', 'Corte CNC com Usinagem'), ('CNC / Dobra / Usinagem', 'Corte CNC com Dobra e Usinagem'), ('Manual', 'Corte Manual'), ('Manual / Dobra', 'Corte Manual com Dobra'), ('Manual / Usinagem', 'Corte Manual com Usinagem'), ('Manual / Dobra / Usinagem', 'Corte Manual com Dobra e Usinagem')], max_length=25)),
                ('file', models.FileField(upload_to=produtos.models.Arquivo.filePath)),
                ('dateCriacao', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
    ]
