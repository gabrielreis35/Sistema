# Generated by Django 3.2.7 on 2021-10-01 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0023_arquivo_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='produto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.produto'),
        ),
    ]
