from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import t
from .models import Destination

def home(request):
    return render(request, 'planner/home.html')

def destinations(request):
    all_destinations = Destination.objects.all()
    return render(request, 'planner/destinations.html', {'destinations': all_destinations})
def trips(request):
    # Logic for displaying trips
    return render(request, 'planner/trips.html')
def login_view(request):
    # Logic for user login
    return render(request, 'planner/login.html')
# Create your views here.
