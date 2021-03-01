from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors

# Create your views here.
def index(request):
    context = {
        "books": Books.objects.all()
    }
    return render(request, "index.html", context)

def add_book(request):
    Books.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
    )
    return redirect('/')

def book_info(request, book_id):
    thisBook = Books.objects.get(id=book_id)
    non_assoc_authors = Authors.objects.exclude(books=thisBook)
    context = {
        'book' : Books.objects.get(id = book_id),
        'authors' : Books.objects.get(id = book_id).authors.all(),
        'all_authors' : Authors.objects.all(),
        'non_authors': non_assoc_authors,
    }
    return render(request, 'book_info.html', context)

def append_authors(request, book_id):
    option = Authors.objects.get(id = request.POST['select_author'])
    Books.objects.get(id = book_id).authors.add(option)
    return redirect(f'/book_info/{book_id}')

def authors(request):
    context = {
        'authors': Authors.objects.all()
    }
    return render(request, 'authors.html', context)

def add_author(request):
    new_author = Authors.objects.create(fname=request.POST['fname'], lname=request.POST['lname'], 
        notes=request.POST['notes'])
    return redirect('/authors')

def author_info(request, author_id):
    context = {
        'author': Authors.objects.get(id= author_id),
        'author_books': Authors.objects.get(id = author_id).books.all(),
        'all_books': Books.objects.all(),
        
    }
    return render(request, 'author_info.html', context)

def append_books(request, author_id):
    option = Books.objects.get(id = request.POST['select_book'])
    Authors.objects.get(id = author_id).books.add(option)
    return redirect(f'/author_info/{author_id}')

