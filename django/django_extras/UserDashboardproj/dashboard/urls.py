from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_index),
    path('admin', views.dashboard_admin),
]
