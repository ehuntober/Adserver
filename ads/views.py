from django.shortcuts import render
from django.db.models import Count , Sum 
from rest_framework.views import APIView

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ads.models import Ad , UserProfile
from ads.serializers import AdSerializer , UserProfileSerializer
from django.contrib.auth.models import User

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
    
    
class UserProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
    
    
class AdvertiserDashboardAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    
    def get_queryset(self):
        return Ad.objects.filter(adverster=self.request.user)
    
    
class 
        

    
    