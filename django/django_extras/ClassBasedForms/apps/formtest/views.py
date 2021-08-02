from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def index(request):
    forms = RegisterForm()
    context = {
        'regForm': forms,
    }
    return render(request, "index.html", context)