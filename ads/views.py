from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ads.models import Ad 
from ads.serializers import AdSerializer

class AdListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(advertiser=self.request.user)
        

class AdRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    