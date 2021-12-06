from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time
from script.MyIllini import findClass, findClasss
from .models import Course
# Create your views here.   
# views ()
def home(request):
    context = {
        'title' : 'wow',
    }
    return render(request, 'website/home.html',context)
def output(request):
    password = request.POST.get("password")
    courses = findClass(request.user.email,password)
    for course in courses:
        Course.objects.create(name = course[0], number = course[1], instructor = course[2], location = course[3], time = course[4], final = course[5], owner = request.user)
    context={
        'title': "Crewvio",
        'list': list
    }
    return render(request, 'website/output.html',context)

def result(request):
    context = {
        'courses': Course.objects.filter(owner = request.user)
    }
    return render(request, 'website/result.html', context)
