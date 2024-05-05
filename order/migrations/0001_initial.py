# Generated by Django 4.2.11 on 2024-05-05 16:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(default=order.models.PurchaseOrder.get_po_number, editable=False, max_length=20, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('expected_delivery_date', models.DateField(blank=True, null=True)),
                ('actual_delivery_date', models.DateField(blank=True, null=True)),
                ('items', models.JSONField(default=dict)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('process', 'In Process'), ('completed', 'Completed'), ('return', 'Return'), ('canceled', 'Canceled')], default='pending', max_length=20)),
                ('quality_rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_orders', to='vendor.vendor')),
            ],
        ),
    ]
