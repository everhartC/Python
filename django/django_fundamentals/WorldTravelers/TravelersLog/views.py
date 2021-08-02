from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from login_app.models import User, UserManager

# Create your views here.
def travelersIndex(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_trips': Trip.objects.all(),
    }

    return render(request, "travelers.html", context)

def addTrip(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    newTrip = Trip.objects.create(location=request.POST['location'], date=request.POST['date'], traveler=logged_user)
    return redirect('/travelers')