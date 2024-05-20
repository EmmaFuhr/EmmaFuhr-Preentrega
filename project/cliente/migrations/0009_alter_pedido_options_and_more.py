# Generated by Django 5.0.4 on 2024-05-20 00:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0004_articulo_stock'),
        ('cliente', '0008_alter_pedido_cantidad'),
        ('vendedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ('-fecha_creacion',)},
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fecha_actualizacion',
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_creacion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, editable=False, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='total_venta',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=20, verbose_name='Total venta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.DO_NOTHING, to='vendedor.vendedor', verbose_name='Vendedor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='articulo',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.DO_NOTHING, to='articulo.articulo', verbose_name='Artículo'),
            preserve_default=False,
        ),
    ]
