from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth.views import LoginView
from .import views

urlpatterns = [
    #/homesapp/
    url(r'^$',views.IndexView.as_view(),name='index'),
   #/homesapp/1
   url(r'^(?P<pk>[0-9]+)/$',views.LocationView.as_view(),name='property'),
   #/homesapp/1/2
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/$',views.PropertyDetail.as_view(),name='propertyview'),
    url(r'^signup/$',views.signup_view,name="signup"),
    url(r'^home/',views.home_view,name="home"),
    url(r'^login/$',views.login_view,name="login")
]