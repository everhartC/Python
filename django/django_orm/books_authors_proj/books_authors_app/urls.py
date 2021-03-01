from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book, name="add_book"),
    path('book_info/<int:book_id>/append_authors', views.append_authors),
    path('book_info/<int:book_id>', views.book_info),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('author_info/<int:author_id>/append_books', views.append_books),
    path('author_info/<int:author_id>', views.author_info),
]