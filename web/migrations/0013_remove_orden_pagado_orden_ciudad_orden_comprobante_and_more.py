# Generated by Django 5.1.6 on 2025-03-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_orden_ordenitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='pagado',
        ),
        migrations.AddField(
            model_name='orden',
            name='ciudad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orden',
            name='comprobante',
            field=models.ImageField(blank=True, null=True, upload_to='comprobantes/'),
        ),
        migrations.AddField(
            model_name='orden',
            name='direccion',
            field=models.CharField(default='Sin dirección', max_length=255),
        ),
    ]
