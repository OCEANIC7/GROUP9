from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Auth (SAFE: keep Django auth views)
    path('register/', views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='planner/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),

    # Dashboards
    path('dashboard/', views.dashboard_redirect, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),

    # Trips
    path('trips/', views.trips, name='trips'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('trips/edit/<int:trip_id>/', views.edit_trip, name='edit_trip'),
    path('trips/delete/<int:trip_id>/', views.delete_trip, name='delete_trip'),

    # Destinations
    path('destinations/', views.destinations, name='destinations'),
]
