from django.urls import path,include
from . views import PurchaseOrderAcknowledge 
urlpatterns = [
    path('purchase_orders/<slug:po_id>/acknowledge/', PurchaseOrderAcknowledge.as_view(),name='purchase_acknowledge')
]
