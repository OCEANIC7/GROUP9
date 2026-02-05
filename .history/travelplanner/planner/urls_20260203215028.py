# planner/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

/urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('trips/', views.trips, name='trips'),
    path('trips/edit/<int:trip_id>/', views.edit_trip, name='edit_trip'),
    path('trips/delete/<int:trip_id>/', views.delete_trip, name='delete_trip'),
   path('login/', auth_views.LoginView.as_view(template_name='planner/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip_detail'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

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
