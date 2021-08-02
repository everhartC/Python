from django.urls import path
from . import views

# ONLY COMES HERE IF URL = localhost:8000/travelers/
urlpatterns = [
    path('', views.travelersIndex),
    path('addTrip', views.addTrip),
]