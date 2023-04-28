from rest_framework import serializers
from ads.models import Ad , UserProfile

class AdSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ad
        fields = '__all__'
        

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = '__all__'