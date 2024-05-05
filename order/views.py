from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.views import APIView
from .models import PurchaseOrder
from . serializers import PurchaseOrderSerializer
from . filters import PurchaseOrderFilter
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PurchaseOrderFilter

class PurchaseOrderAcknowledge(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
    def patch(self,request,po_id):
        po_obj=PurchaseOrder.objects.filter(pk=po_id).first()
        if not po_obj:
            return JsonResponse({"error":"No purchase order found with that id"},status=404)
        
        try:
            po_obj.acknowledgment_date=timezone.now()
            po_obj.save()
            serializer=PurchaseOrderSerializer(po_obj,many=False)
            return JsonResponse(serializer.data, status=200)
        except Exception as e:
            print("Error in updating PO",e)
            return JsonResponse({"error":str(e)},status=500)