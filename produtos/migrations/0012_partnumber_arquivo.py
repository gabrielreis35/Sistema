# Generated by Django 3.2.8 on 2021-12-14 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0011_arquivo_tipoarquivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnumber',
            name='arquivo',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='produtos.arquivo'),
            preserve_default=False,
        ),
    ]
