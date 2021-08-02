from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Count
from django.contrib import messages
from .models import UserManager, BookManager, User, Book

# Create your views here.
def index(request):
    return render(request, "index.html")

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
        request.session['name'] = new_user.fname
        # messages.success(request, "You have successfully registered!")
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

def books(request):
    if not request.session['user_id']:
        return redirect('/')
    listlikes = Book.objects.filter().annotate(num_likes=Count('users_who_fav')).order_by('-num_likes')
    context = {
        'all_books': Book.objects.all().order_by('-created_at'),
        'this_user': User.objects.get(id=request.session['user_id']),
        'likes_per_book': listlikes,
    }
    return render(request, "bookWall.html", context)

def logout(request):
    try:
        del request.session['user_id']
        messages.success(request, "Successfully logged out")
    except KeyError:
        pass
    return redirect('/')

# POST - Received from addBook form in bookWall
def addBook(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        current_user = User.objects.get(id=request.session['user_id'])
        new_book = Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
            uploaded_by = current_user,
        )
        current_user.fav_books.add(new_book)
        return redirect('/books')

def addFavorite(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/books')

    current_user = User.objects.get(id=request.session['user_id'])
    favBook = Book.objects.get(id=book_id)
    current_user.fav_books.add(favBook)
    return redirect('/books')


def bookInfo(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'this_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "bookinfo.html", context)

def editBook(request, book_id):
    book_to_edit = Book.objects.get(id=book_id)
    book_to_edit.desc = request.POST['editdesc']
    book_to_edit.save()
    return redirect(f'/books')

def unFavorite(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/books')

    current_user = User.objects.get(id=request.session['user_id'])
    favBook = Book.objects.get(id=book_id)
    current_user.fav_books.remove(favBook)
    return redirect(f'/books/{book_id}')



