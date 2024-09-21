from django.shortcuts import render
from django.http import  JsonResponse
from django.shortcuts import redirect, render

from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
 

# Create your views here.

def login_page(request):
  if request.user.is_authenticated:
    return redirect("/")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request)
        messages.success(request,"Logged in Successfully")
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"login.html")
 