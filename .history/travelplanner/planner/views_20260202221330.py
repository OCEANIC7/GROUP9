from django.shortcuts import render

def home(request):
    return render(request, 'planner/home.html')


# Create your views here.
