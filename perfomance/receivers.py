from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from order.models import PurchaseOrder
from django.db import transaction

# Pre-save signal
@receiver(pre_save, sender=PurchaseOrder)
@transaction.atomic
def PurchaseOrder_pre_save(sender, instance, **kwargs):
    old_obj = PurchaseOrder.objects.filter(pk=instance.pk).first()
    instance.old_obj = old_obj

# Post-save signal      
@receiver(post_save, sender=PurchaseOrder)
@transaction.atomic
def PurchaseOrder_post_save(sender, instance, **kwargs):
    from . views import cal_on_time_delivery_rate,cal_quality_rating_avg,cal_average_response_time,cal_fulfilment_rate 
    old_obj = instance.old_obj
    if old_obj:
        if instance.status == 'completed' and old_obj.status != 'completed':
            cal_on_time_delivery_rate(instance)
            cal_quality_rating_avg(instance)
        if old_obj.acknowledgment_date != instance.acknowledgment_date and instance.acknowledgment_date != None:
            cal_average_response_time(instance)
        cal_fulfilment_rate(instance)
    else:
        if instance.status == 'completed':
            cal_on_time_delivery_rate(instance)
            cal_quality_rating_avg(instance)
        cal_fulfilment_rate(instance)
        
