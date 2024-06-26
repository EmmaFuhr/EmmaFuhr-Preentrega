# Generated by Django 5.0.4 on 2024-05-17 18:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_alter_cliente_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_actualizacion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, editable=False, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cantidad',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
    ]
