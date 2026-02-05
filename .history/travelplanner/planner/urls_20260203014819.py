# planner/urls.py
from django.urls import path
from . import views
fr

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('trips/', views.trips, name='trips'),
    path('login/', views.login_view, name='login'),
]

