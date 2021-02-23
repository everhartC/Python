from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('userTicketSale', views.user),
    path('formSubmission', views.formSubmission),
    path('<str:Anything>', views.fourOfour),
]