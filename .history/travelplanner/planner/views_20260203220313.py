from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import TripForm
from .models import Trip, Destination


@login_required
def dashboard_redirect(request):
    if request.user.groups.filter(name='Admin').exists():
        return redirect('admin_dashboard')
    else:
        return redirect('user_dashboard')

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'dashboards/admin_dashboard.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # 🔥 ADD USER TO "User" GROUP
        user_group = Group.objects.get(name='User')
        user.groups.add(user_group)

        return redirect('login')

    return render(request, 'planner/register.html')

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

    return render(
        request,
        'planner/delete_trip.html',
        {
            'trip': trip
        }
    )
@login_required
def trip_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id, user=request.user)

    return render(
        request,
        'planner/trip_detail.html',
        {
            'trip': trip
        }
    )
    
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'planner/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'planner/login.html')

@login_required
def user_dashboard(request):
    return render(request, 'dashboards/user_dashboard.html')

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'dashboards/admin_dashboard.html')