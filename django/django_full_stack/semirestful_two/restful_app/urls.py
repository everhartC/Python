from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.myRedirect),
    path('shows', views.index),   # Display All Shows, everything in the DB
    path('shows/new', views.addNewShow),
    path('shows/create', views.createShow),
    path('shows/<int:showID>',views.showPage),
    path('shows/<int:showID>/edit', views.editShow),
    path('shows/<int:showID>/update', views.updateShow),
    path('shows/<int:showID>/delete', views.deleteShow),
]

