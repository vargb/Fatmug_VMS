from rest_framework import generics,response,permissions
from vendors.models import Vendor, HistoricalPerformance
from vendors.serializers import (
    VendorSerializer,
    VendorPerformanceSerializer,
    HistoricalPerformanceSerializer,
)
    
class VendorListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    
class VendorActionView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer


class VendorPerformanceHistoryView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    
    
    
