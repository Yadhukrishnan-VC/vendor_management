from rest_framework import serializers
from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    acknowledgment_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
