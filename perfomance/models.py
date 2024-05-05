from django.db import models
from vendor.models import Vendor
from django.core.validators import MinValueValidator
# Create your models here.

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performances')
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    quality_rating_avg = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    average_response_time = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    fulfillment_rate = models.FloatField(default=0, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.vendor} - {self.date}"