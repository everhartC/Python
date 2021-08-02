from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home),
    path('addCourse', views.addCourse),
    path('courses/<int:courseID>/delete', views.deleteCourse)
]