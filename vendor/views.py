from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework import viewsets
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class VendorViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class VendorViewPerfomance(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'pk'
