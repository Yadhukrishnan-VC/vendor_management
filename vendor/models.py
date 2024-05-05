from django.db import models
import uuid
from django.core.validators import MinValueValidator

# Create your models here.

class Vendor(models.Model):
    
    def get_vendor_code():
        return str(uuid.uuid4().hex)[:10].upper()
    
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=10, unique=True, default=get_vendor_code, editable=False)
    on_time_delivery_rate = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    quality_rating_avg = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    average_response_time = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    fulfillment_rate = models.FloatField(default=0, validators=[MinValueValidator(0.0)])


    def __str__(self):
        return self.name
