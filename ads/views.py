from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ads.models import Ad 
from ads.serializers import AdSerializer

class AdListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    