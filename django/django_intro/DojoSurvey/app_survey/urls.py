from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('survey', views.survey),
    path('result', views.result),
]