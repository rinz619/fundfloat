from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from superadmin import views


app_name = 'superadmin'

urlpatterns = [
    path('',views.index.as_view(),name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('profile', views.profile.as_view(), name='profile'),

    path('Dashboard', views.dashboard.as_view(), name='dashboard'),

    
]