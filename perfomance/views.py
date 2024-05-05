from django.shortcuts import render
from vendor.models import Vendor
from order.models import PurchaseOrder
from . models import HistoricalPerformance 
from django.db.models import F,Avg,ExpressionWrapper,DurationField


""" Update On-Time Delivery Rate when a PO status changes to 'completed'"""
def cal_on_time_delivery_rate(instance):
    completed_purchases = PurchaseOrder.objects.filter(vendor=instance.vendor,status='completed')
    on_time_deliveries = completed_purchases.filter(actual_delivery_date__lte=F('expected_delivery_date'))
    on_time_delivery_rate = (on_time_deliveries.count() / completed_purchases.count()) * 100
    instance.vendor.on_time_delivery_rate = on_time_delivery_rate
    instance.vendor.save()
    vendor_pefo = HistoricalPerformance.objects.update_or_create(
        vendor = instance.vendor,
        defaults={
            'on_time_delivery_rate': on_time_delivery_rate,
        }
    )
    

""" Update Quality Rating Average when a completed PO has a quality rating"""    
def cal_quality_rating_avg(instance):
    completed_purchases_with_rating = PurchaseOrder.objects.filter(
        vendor=instance.vendor,
        status='completed'
    ).aggregate(
        quality_rating_avg=Avg('quality_rating')
    )
    instance.vendor.quality_rating_avg = completed_purchases_with_rating['quality_rating_avg']
    instance.vendor.save()
    vendor_pefo = HistoricalPerformance.objects.update_or_create(
        vendor = instance.vendor,
        defaults={
            'quality_rating_avg': completed_purchases_with_rating['quality_rating_avg'],
        }
    )
    
""" Update Average Response Time when a PO is acknowledged by the Vendor """
def cal_average_response_time(instance):
    acknowledged_purchases = PurchaseOrder.objects.filter(
        vendor=instance.vendor
    ).annotate(time_difference=ExpressionWrapper(
        F('acknowledgment_date') - F('issue_date'),
        output_field=DurationField()
    )).aggregate(avg_time_difference=Avg('time_difference'))
    
    instance.vendor.average_response_time = acknowledged_purchases['avg_time_difference'].total_seconds()
    instance.vendor.save()
    vendor_pefo = HistoricalPerformance.objects.update_or_create(
        vendor = instance.vendor,
        defaults={
            'average_response_time': acknowledged_purchases['avg_time_difference'].total_seconds(),
        }
    )
    

""" Update Fulfilment Rate upon any change in PO status """
def cal_fulfilment_rate(instance):
    total_purchases = PurchaseOrder.objects.filter(vendor=instance.vendor).count()
    fulfilled_purchases = PurchaseOrder.objects.filter(
        vendor=instance.vendor,
        status='completed'
    ).count()
    fulfillment_rate = ((fulfilled_purchases / total_purchases) * 100) if total_purchases > 0 else 0
    instance.vendor.fulfillment_rate = fulfillment_rate
    instance.vendor.save()
    vendor_pefo = HistoricalPerformance.objects.update_or_create(
        vendor = instance.vendor,
        defaults={
            'fulfillment_rate': fulfillment_rate,
        }
    )