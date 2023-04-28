from django.urls import path
from ads.views import AdListCreateAPIView , AdRetrieveUpdateDestoryAPIView ,UserProfileRetrieveUpdateAPIView ,\
    AdvertiserDashboardAPIView , AdAnalyticsAPIView

from django.conf.urls import url 
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title = 'Ads Management API')

urlpatterns = [
    path('ads/',AdListCreateAPIView.as_view(), name='ad_list_create'),
    path('ads/<int:pk>/',AdRetrieveUpdateDestoryAPIView.as_view(), name='ad_retrieve_update_destory'),
    
    path('user/profile/',UserProfileRetrieveUpdateAPIView.as_view(),name='user_profile'),
    path('advertiser/dashboard/',AdvertiserDashboardAPIView.as_view(),name='advertiser_dashboard'),
    path('ads/analytics/',AdAnalyticsAPIView.as_view(),name='ad_analytics'),
    
    
    url(r'^docs/$',schema_view)
    
    
]
