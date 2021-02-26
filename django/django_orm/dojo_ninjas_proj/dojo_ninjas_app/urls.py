from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index),
    path('ninjas/add_ninja', views.add_ninja, name="add_ninja"),
    path('dojos/add_dojo', views.add_dojo, name="add_dojo"),
]