# Generated by Django 3.2.8 on 2021-12-17 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0016_partnumber_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnumber',
            name='arquivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.arquivo'),
        ),
    ]