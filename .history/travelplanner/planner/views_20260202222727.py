from django.shortcuts import render
from .models import Destination

def home(request):
    return render(request, 'planner/home.html')

def destinations(request):
    # Logic for displaying destinations
    return render(request, 'planner/destinations.html', {'destinations': a})
def trips(request):
    # Logic for displaying trips
    return render(request, 'planner/trips.html')
def login_view(request):
    # Logic for user login
    return render(request, 'planner/login.html')
# Create your views here.
