# Generated by Django 3.2.7 on 2021-09-24 12:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('colaborator', '0001_initial'),
        ('produtos', '0015_produto_responsavel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=20)),
                ('dateCriacao', models.DateTimeField(auto_now_add=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='numDentes',
        ),
        migrations.AddField(
            model_name='item',
            name='dateCriacao',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 9, 24, 12, 9, 42, 533813, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='dateUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='item',
            name='revisao',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='partNumber',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='colaborator.colaborador'),
        ),
    ]