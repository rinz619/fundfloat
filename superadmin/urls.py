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

    path('dashboard', views.dashboard.as_view(), name='dashboard'),

    
    path('courselist', views.courselist.as_view(), name='courselist'),
    path('coursecreate', views.coursecreate.as_view(), name='coursecreate'),
    path('courseedit/<int:id>', views.coursecreate.as_view(), name='courseedit'),
     
    path('instructorlist', views.instructorlist.as_view(), name='instructorlist'),
    path('instructorcreate', views.instructorcreate.as_view(), name='instructorcreate'),
    path('editinstructor/<int:id>', views.instructorcreate.as_view(), name='editinstructor'),

    
]