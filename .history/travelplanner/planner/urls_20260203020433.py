# planner/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('trips/', views.trips, name='trips'),
    path('trips/edit/<int:trip_id>/', views.edit_trip, name='edit_trip'),
    
   path('login/', auth_views.LoginView.as_view(template_name='planner/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]

