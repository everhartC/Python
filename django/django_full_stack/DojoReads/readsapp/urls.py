from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('logout', views.logout),
    path('books/add', views.addBookPage),
    path('addbook', views.addBook),
    path('books/<int:bookid>', views.bookInfo),
    path('users/<int:uID>', views.userPage),
]