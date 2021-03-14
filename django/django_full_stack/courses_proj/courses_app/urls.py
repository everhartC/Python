from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses', views.index),
    path('courses/addCourse', views.addCourse),
    path('courses/<int:courseID>', views.comments),
    path('courses/<int:courseID>/comment', views.addComment),
    path('courses/destroy/<int:courseID>', views.destroyCourse),
]