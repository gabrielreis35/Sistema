# Generated by Django 3.2.8 on 2021-12-17 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0015_auto_20211216_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnumber',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produtos.produto'),
            preserve_default=False,
        ),
    ]