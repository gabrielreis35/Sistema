# Generated by Django 3.2.8 on 2021-12-02 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_partnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='partNumber',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tipoFabricacao',
        ),
    ]
