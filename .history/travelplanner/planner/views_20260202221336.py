from django.shortcuts import render

def home(request):
    return render(request, 'planner/home.html')

def destinations(request):
# Create your views here.
