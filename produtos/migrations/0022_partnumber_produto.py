# Generated by Django 3.2.8 on 2021-12-22 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0021_auto_20211222_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnumber',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produtos.produto'),
            preserve_default=False,
        ),
    ]
