from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages

# Create your views here.

# Route to send users to main page to either Login or 
# Register. Register is form/POST
def index(request):
    context = {
        'all_users': User.objects.all(),
    }
    return render(request, "index.html", context)

# POST data sent from registration form
#  (fname, lname, email, password, confpw)
def register(request):
    errors = User.objects.validator(request.POST)
    # If errors in form, display error message and redirect to index
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    # If not, add POST data and create user object. 
    # Redirect to index for now
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/travelers')

def login(request):
    if request.method == "GET": # if GET then it's not from POST form
        redirect('/')
    if not User.objects.authenticate(
        request.POST['email'], request.POST['password']):
        messages.error(request, "Invalid Email/Password")
        return redirect('/')

    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in")
    return redirect('/travelers')
    

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')




