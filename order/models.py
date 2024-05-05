from django.db import models
from vendor.models import Vendor
import uuid
from django.core.validators import MinValueValidator

# Create your models here.

class PurchaseOrder(models.Model):
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('process', 'In Process'),
        ('completed', 'Completed'),
        ('return', 'Return'),
        ('canceled', 'Canceled'),
    ]
    
    def get_po_number():
        return str(uuid.uuid4().hex)[:20].upper()

    po_number = models.CharField(max_length=20, unique=True, default=get_po_number,editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery_date = models.DateField(null=True, blank=True)    
    actual_delivery_date = models.DateField(null=True, blank=True)
    items = models.JSONField(default=dict)
    quantity = models.IntegerField(validators=[MinValueValidator(0.0)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True,validators=[MinValueValidator(0.0)])
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number