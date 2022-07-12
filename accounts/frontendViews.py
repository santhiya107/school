from urllib import response
from . forms import *
from django.shortcuts import render,redirect
from .models import *
import requests
import json
def land(request):
    return render(request,'accounts/content.html')
def home(request):
    return render(request,'base.html')
def signup(request): 
    form=signup_form(data=request.POST)    
    return render(request,'accounts/signup.html',{'form':form})  
def simple(request):      
    form=login_form()
    return render(request,'accounts/login.html',{'form':form})
def profile(request):    
    return render(request,'accounts/profile.html')
def userdetails(request):    
    return render(request,'accounts/userdetails.html')

def staff(request):
    return render(request,'accounts/staffs.html')