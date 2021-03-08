from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('shows', views.AllShows),
    path('shows/new', views.AddNewShow), # GET
    path('shows/create', views.CreateNewShow), # POST
    path('shows/<int:id>', views.TvShow), # GET
    path('shows/<int:id>/edit', views.EditShow), # GET
    path('shows/<int:id>/update', views.UpdateShow), # POST
    path('shows/<int:id>/destroy', views.DeleteShow), # POST
]