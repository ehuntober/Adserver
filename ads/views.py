from django.shortcuts import render
from django.db.models import Count , Sum 
from rest_framework.views import APIView
from rest_framework.response import Response 


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
        return Ad.objects.filter(advertiser=self.request.user)
    
    
class AdAnalyticsAPIView(APIView):
    def get(self, request):
        ad_count = Ad.objects.count()
        click_count = Ad.objects.aggregate(Sum('click_count'))['click_count__sum']
        impression_count = Ad.objects.aggregate(Sum('impression_count'))['impression_count__sum']
        advertiser_count = Ad.objects.values('advertiser').distinct().count()
        top_ads = Ad.objects.annotate(click_sum=Sum('click_count')).order_by('-click_sum')[:5]
        
        return Response({
            'ad_count': ad_count,
            'click_count': click_count,
            'impression_count': impression_count,
            'advertiser_count': advertiser_count,
            'top_ads':AdSerializer(top_ads,many=True).data
        })
        
        

    
    