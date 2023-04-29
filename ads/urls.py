from django.urls import path ,re_path as url
from ads.views import AdListCreateAPIView , AdRetrieveUpdateDestoryAPIView ,UserProfileRetrieveUpdateAPIView ,\
    AdvertiserDashboardAPIView , AdAnalyticsAPIView


# from django.conf.urls import url 
 
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title = 'Ads Management API')


# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Ads Management API",
        default_version='v1',
        description="Welcome to Adserver",
        terms_of_service="https://www.adserver.org",
        contact=openapi.Contact(email="www.adserver.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('ads/',AdListCreateAPIView.as_view(), name='ad_list_create'),
    path('ads/<int:pk>/',AdRetrieveUpdateDestoryAPIView.as_view(), name='ad_retrieve_update_destory'),
    
    path('user/profile/',UserProfileRetrieveUpdateAPIView.as_view(),name='user_profile'),
    path('advertiser/dashboard/',AdvertiserDashboardAPIView.as_view(),name='advertiser_dashboard'),
    path('ads/analytics/',AdAnalyticsAPIView.as_view(),name='ad_analytics'),
    
    
    # url(r'^docs/$',schema_view),
    url(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'), 
    
    
]
