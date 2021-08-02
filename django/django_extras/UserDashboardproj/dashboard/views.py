from django.shortcuts import render, redirect, HttpResponse
from login.models import User


# Create your views here.
def dashboard_index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'users': User.objects.all()
    }
    return render(request, "dashboard_index.html", context)

def dashboard_admin(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.session['level'] is False:
        return redirect('/')
    context = {
        'users': User.objects.all()
    }
    return render(request, "dashAdmin.html", context)