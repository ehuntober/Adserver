from django.contrib import admin

# Register your models here.

from .models import Ad  ,UserProfile

admin.site.register(Ad)
admin.site.register(UserProfile)
