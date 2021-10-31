from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time
from script.MyIllini import findClass, findClasss
# Create your views here.   
# views ()
def home(request):
    context = {
        'title' : 'wow',
    }
    return render(request, 'website/home.html',context)
def output(request):
    password = request.POST.get("password")
    list = findClass(request.user.email,password)
    context={
        'title': "Crewvio",
        'list': list
    }
    return render(request, 'website/output.html',context)
