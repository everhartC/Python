from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def root(request):
    return redirect('/suckers')

def index(request):
    if request.method == "POST":
        errors = Sucker.objects.SuckerValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/suckers')
        Sucker.objects.create(email=request.POST['email'], password=request.POST['password'])
        return redirect('/suckers') # GET request
    else:
        print("Welcome to the site!")
        context = {
            'Suckers': Sucker.objects.all()
        }
    return render(request, "index.html", context)