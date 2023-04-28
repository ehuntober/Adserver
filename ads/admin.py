from django.contrib import admin

# Register your models here.

from .models import Ad  ,UserProfile , AdvertiserReview

admin.site.register(Ad)
admin.site.register(UserProfile)
admin.site.register(AdvertiserReview)
