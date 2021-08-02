from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('recipe/<int:recipeID>', views.oneRecipe),
    path('recipe/edit', views.update),
    path('recipe/destroy', views.destroy),
]