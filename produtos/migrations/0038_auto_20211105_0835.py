# Generated by Django 3.2.8 on 2021-11-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0037_auto_20211104_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriaproduto',
            name='sigla',
            field=models.CharField(default=0, max_length=5, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classeproduto',
            name='sigla',
            field=models.CharField(default=0, max_length=3, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segmento',
            name='sigla',
            field=models.CharField(default=0, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipoproduto',
            name='sigla',
            field=models.CharField(default=0, max_length=3, unique=True),
            preserve_default=False,
        ),
    ]