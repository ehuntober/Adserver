from django.db import models

# Create your models here.

from django.contrib.auth.models import User 

class Ad(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="ads")
    url = models.URLField()
    adverster = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    