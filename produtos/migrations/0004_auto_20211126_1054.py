# Generated by Django 3.2.8 on 2021-11-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_rename_nomeproduto_produtocliente_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='comprimento',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='volume',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
