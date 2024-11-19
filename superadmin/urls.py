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

    
    path('userlist', views.userlist.as_view(), name='userlist'),
    path('usercreate', views.usercreate.as_view(), name='usercreate'),
    path('useredit/<int:id>', views.usercreate.as_view(), name='useredit'),
    
    path('courselist', views.courselist.as_view(), name='courselist'),
    path('coursecreate', views.coursecreate.as_view(), name='coursecreate'),
    path('courseedit/<int:id>', views.coursecreate.as_view(), name='courseedit'),
     
    path('instructorlist', views.instructorlist.as_view(), name='instructorlist'),
    path('instructorcreate', views.instructorcreate.as_view(), name='instructorcreate'),
    path('editinstructor/<int:id>', views.instructorcreate.as_view(), name='editinstructor'),

    path('paymentlist', views.paymentlist.as_view(), name='paymentlist'),

         
    path('categorybloglist', views.categorybloglist.as_view(), name='categorybloglist'),
    path('categoryblogcreate', views.categoryblogcreate.as_view(), name='categoryblogcreate'),
    path('categoryblogedit/<int:id>', views.categoryblogcreate.as_view(), name='categoryblogedit'),
    
         
    path('bloglist', views.bloglist.as_view(), name='bloglist'),
    path('blogcreate', views.blogcreate.as_view(), name='blogcreate'),
    path('blogedit/<int:id>', views.blogcreate.as_view(), name='blogedit'),

    
]