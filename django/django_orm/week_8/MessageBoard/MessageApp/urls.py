from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('newMessage', views.newMessage),
    path('message/<int:messageid>', views.oneMessage),
    path('addComment', views.addComment),
]
