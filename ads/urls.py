from django.urls import path
from ads.views import AdListCreateAPIView , AdRetrieveUpdateDestoryAPIView ,UserProfileRetrieveUpdateAPIView , AdvertiserDashboardAPIView

urlpatterns = [
    path('ads/',AdListCreateAPIView.as_view(), name='ad_list_create'),
    path('ads/<int:pk>/',AdRetrieveUpdateDestoryAPIView.as_view(), name='ad_retrieve_update_destory'),
    
    path('user/profile/',UserProfileRetrieveUpdateAPIView.as_view(),name='user_profile'),
    
    
]
