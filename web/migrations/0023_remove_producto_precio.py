# Generated by Django 5.1.6 on 2025-03-06 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_remove_producto_descuento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
    ]
