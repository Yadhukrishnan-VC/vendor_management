from django.urls import path,include
from . views import VendorViewPerfomance 
urlpatterns = [
    path('vendors/<slug:pk>/perfomance/', VendorViewPerfomance.as_view(),name='purchase_acknowledge')
]
