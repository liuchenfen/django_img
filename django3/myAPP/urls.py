from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include

from . import views

urlpatterns = [
    path('',views.index),
    re_path('image/(?P<width>[0-9]+)x(?P<height>[0-9]+)',views.image,name="placeholder"),
    
#     url(r'^$', views.index),
#     url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$',views.image),
]