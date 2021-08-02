from django.shortcuts import render, redirect
from .models import User, Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all(),
        'post_form': PostForm(),
    }
    return render(request, "posts.html", context)

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
        new_user.first_name = new_user.first_name.title()
        request.session['user_id'] = new_user.id
        request.session['name'] = new_user.first_name
        messages.success(request, "You have successfully registered!")
        return redirect('/posts')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, "Invalid Email or Password")
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    request.session['name'] = user.first_name
    # messages.success(request, "You have successfully logged in")
    return redirect('/posts')

def logout(request):
    try:
        del request.session['user_id']
        messages.success(request, "Successfully logged out")
    except KeyError:
        pass
    return redirect('/')


def posts(request):
    this_user = User.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            Post.objects.create(content=request.POST['content'], poster=this_user)
        return redirect('/posts')

    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'posts_index.html', context)


