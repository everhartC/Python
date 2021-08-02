from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from dashboard.models import Message, Comment

# Create your views here.

def index(request):
    return render(request, "index.html")

# POST data sent from registration form
#  (fname, lname, email, password, confpw)
def register(request):
    if request.method == "GET":
        return render(request, "register.html")
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
        new_user.fname = new_user.fname.title()
        request.session['user_id'] = new_user.id
        if new_user.id != 1:
            new_user.level = False
            new_user.save()
            return redirect('/dashboard')
        else:
            new_user.level = True
            new_user.save()
            request.session['level'] = "Admin"
        request.session['name'] = new_user.fname
        messages.success(request, "You have successfully registered!")
        return redirect('/dashboard/admin')

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, "Invalid Email or Password")
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    if user.level == False:
        request.session['user_id'] = user.id
        request.session['level'] = user.level
        return redirect('/dashboard')
    else:
        request.session['user_id'] = user.id
        request.session['level'] = user.level
    # messages.success(request, "You have successfully logged in")
        return redirect('/dashboard/admin')

def logout(request):
    try:
        del request.session['user_id']
        messages.success(request, "Successfully logged out")
    except KeyError:
        pass
    return redirect('/')

# This will always be admin only because admin only can add new users
def addUser(request):
    if request.method == "GET":
        return render(request, "newUserPage.html")
    nuser = User.objects.register(request.POST)
    return redirect('/dashboard/admin')

def showUser(request, id):
    if request.method == "GET":
        context = {
            'this_user': User.objects.get(id=id),
            'all_users': User.objects.all(),
            'messages': Message.objects.all(),
            'comments': Comment.objects.all(),
        }
        return render(request, "UserProfile.html", context)

    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        message = Message.objects.create(
            msg = request.POST['msg'],
            user = user,
        )
        return redirect(f'/users/show/{id}')
    
