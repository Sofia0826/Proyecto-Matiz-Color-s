# Generated by Django 5.1.6 on 2025-03-06 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_remove_carritoitem_color_alter_carritoitem_cantidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='descuento',
        ),
    ]
