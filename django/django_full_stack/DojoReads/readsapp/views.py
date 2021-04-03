from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
# from login.models import *
from django.db.models import Sum


# Create your views here.
def index(request):
    return render(request, "index.html")

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
        new_user.fname = new_user.fname.title()
        request.session['user_id'] = new_user.id
        request.session['name'] = new_user.fname
        messages.success(request, "You have successfully registered!")
        return redirect('/books')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, "Invalid Email or Password")
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    request.session['name'] = user.fname
    # messages.success(request, "You have successfully logged in")
    return redirect('/books')

def logout(request):
    try:
        del request.session['user_id']
        messages.success(request, "Successfully logged out")
    except KeyError:
        pass
    return redirect('/')

def books(request):
    if not request.session['user_id']:
        return redirect('/')

    context = {
        'reviews3': Review.objects.all().order_by('-created_at')[:3:1],
        'this_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, "books.html", context)

def addBookPage(request):
    if not request.session['user_id']:
        return redirect('/books')

    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "add_book.html", context)

def addBook(request):
    if not request.session['user_id']:
        return redirect('/')

    this_user = User.objects.get(id=request.session['user_id'])
    new_book = Book.objects.create(
        title = request.POST['title'],
        author = request.POST['addauthor'],
    )
    new_review = Review.objects.create(
        comment=request.POST['review'],
        rating = request.POST['rating'],
        reviewer = this_user,
        book = new_book,
    )
    request.session['bookid'] = new_book.id

    return redirect(f'/books/{new_book.id}')

def bookInfo(request, bookid):
    book = Book.objects.get(id = bookid)

    context = {
        'book': book,
    }
    return render(request, "book_info.html", context)

def userPage(request, uID):
    if not request.session['user_id']:
        messages.error(request, "User not currently logged in")
        return redirect('/books')
    
    user = User.objects.get(id=uID)
    reviews = user.written_reviews.all()
    context = {
        'user': user,
        'reviews': reviews,
    }
    return render(request, "user_info.html", context)
    


