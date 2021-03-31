from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('logout', views.logout),
    path('addBook', views.addBook),
    path('addFavorite/<int:book_id>', views.addFavorite),
    path('books/<int:book_id>', views.bookInfo),
    path('books/<int:book_id>/edit', views.editBook),
    path('unFavorite/<int:book_id>', views.unFavorite),
]