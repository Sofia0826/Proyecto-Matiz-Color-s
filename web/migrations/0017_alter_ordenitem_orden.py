# Generated by Django 5.1.6 on 2025-03-03 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_ordenitem_precio_alter_ordenitem_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenitem',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='web.orden'),
        ),
    ]
