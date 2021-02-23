from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home),
    path('process_money', views.process_money),
    path('reset', views.reset),
]