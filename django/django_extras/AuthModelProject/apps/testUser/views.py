from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random

# Create your views here.

def index(request):
    User.objects.create_user(first_name="Cameron", last_name = "Everhart", username = str(random.randint(0,100)))
    context = {
        'users': User.objects.all()
    }
    return render(request, "index.html", context)


