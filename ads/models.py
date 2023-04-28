from django.db import models

# Create your models here.

from django.contrib.auth.models import User 

class Ad(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="ads")
    url = models.URLField()
    advertiser = models.ForeignKey(User, on_delete = models.CASCADE)
    
    
    click_count = models.PositiveIntegerField(default=0)
    impression_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username
    

class AdvertiserReview(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.ad.title} - {self.rating}"