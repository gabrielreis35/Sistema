# Generated by Django 3.2.8 on 2021-11-04 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0036_auto_20211104_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClasseProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='codigo',
        ),
        migrations.AddField(
            model_name='produto',
            name='tipoProduto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.tipoproduto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.categoriaproduto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='classeAplicacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.classeproduto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='segmento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.segmento'),
        ),
    ]