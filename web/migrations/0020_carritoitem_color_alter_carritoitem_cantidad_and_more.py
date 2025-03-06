# Generated by Django 5.1.6 on 2025-03-03 22:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_remove_ordenitem_subtotal_ordenitem_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritoitem',
            name='color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carritoitem',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='carritoitem',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='carritoitem',
            name='sesion_id',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
