# Generated by Django 3.2.8 on 2021-10-28 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('colaborator', '0004_auto_20211028_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='dateCriacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
