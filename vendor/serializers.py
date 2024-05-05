from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    
    on_time_delivery_rate = serializers.FloatField(read_only=True)
    quality_rating_avg = serializers.FloatField(read_only=True)
    average_response_time = serializers.FloatField(read_only=True)
    fulfillment_rate = serializers.FloatField(read_only=True)

    class Meta:
        model = Vendor
        fields = '__all__'
