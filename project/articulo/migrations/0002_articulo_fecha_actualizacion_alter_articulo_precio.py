# Generated by Django 5.0.4 on 2024-05-17 18:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='fecha_actualizacion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, editable=False, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio',
            field=models.FloatField(max_length=200, verbose_name='Precio'),
        ),
    ]
