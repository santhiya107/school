from django.urls import path
from.frontendViews import *


urlpatterns=[
    path('',land,name='land'),
    path('home',home,name='home'),
    path('signup',signup,name='signup'),
    path('login',simple,name='simple'),
    path('profile',profile,name='profile'),
     path('userdetails',userdetails,name='userdetails'),
]