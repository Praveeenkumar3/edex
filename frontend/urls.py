from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
    
    path('',views.login,name='login'),
]