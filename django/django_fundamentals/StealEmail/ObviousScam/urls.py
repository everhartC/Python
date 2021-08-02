from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('suckers', views.index),
]
# RESTFUL routing. Main page should be the name of the model plural