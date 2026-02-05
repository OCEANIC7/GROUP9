from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TripForm
from .models import Trip
from .models import Destination

def home(request):
    return render(request, 'planner/home.html')

def destinations(request):
    all_destinations = Destination.objects.all()
    return render(request, 'planner/destinations.html', {'destinations': all_destinations})

@login_required
def trips(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            new_trip = form.save(commit=False)
            new_trip.user = request.user
            new_trip.save()
            return redirect('trips')
    else:
        form = TripForm()

    user_trips = Trip.objects.filter(user=request.user)

    return render(
        request,
        'planner/trips.html',
        {
            'form': form,
            'trips': user_trips
        }
    )
@login_required
def edit_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id, user=request.user)

    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trips')
    else:
        form = TripForm(instance=trip)

    return render(
        request,
        'planner/edit_trip.html',
        {
            'form': form,
            'trip': trip
        }
    )    
@login_required
    def delete_trip(request, trip_id):
        trip = Trip.objects.get(id=trip_id, user=request.user)
        if request.method == 'POST':
            trip.delete()
            return redirect('trips')
        return render(request, 'planner/delete_trip.html', {'trip': trip})
    
def login_view(request):
    # Logic for user login
    return render(request, 'planner/login.html')
# Create your views here.
