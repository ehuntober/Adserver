from rest_framework import serializers
from ads.models import Ad , UserProfile , AdvertiserReview

class AdSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ad
        fields = '__all__'
        

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class AdvertiserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertiserReview
        fields = '__all__'