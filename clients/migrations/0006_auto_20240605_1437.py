# Generated by Django 3.2.25 on 2024-06-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='area_number',
            field=models.IntegerField(verbose_name='Número de Área'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(verbose_name='Teléfono'),
        ),
    ]
