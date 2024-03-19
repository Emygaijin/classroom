from django.shortcuts import render
from .models import Course

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def display(request, serial):
    course = Course.objects.get(serial=serial)
    return render(request, 'display.html', {'course': course})

def home(request):
    return render(request, 'home.html')