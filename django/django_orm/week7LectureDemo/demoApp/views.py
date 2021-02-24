from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def index(request):
    context = {
        'Users': User.objects.all(),
    }
    return render(request, 'home.html', context)