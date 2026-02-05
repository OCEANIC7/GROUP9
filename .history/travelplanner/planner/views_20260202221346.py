from django.shortcuts import render

def home(request):
    return render(request, 'planner/home.html')

def destinations(request):
    # Logic for displaying destinations
    return render(request, 'planner/destinations.html')
def trips(request):
    # Logic for displaying trips
    return render(request, 'planner/trips.html')
# Create your views here.
