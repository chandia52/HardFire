# Generated by Django 3.2.25 on 2024-05-25 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20240523_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='subnombre',
            field=models.CharField(default='', max_length=40),
        ),
    ]
