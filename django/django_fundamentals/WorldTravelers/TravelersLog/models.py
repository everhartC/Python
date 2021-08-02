from django.db import models
from login_app.models import User
# class TripManager(models.Manager)


# Create your models here.
class Trip(models.Model):
    location = models.CharField(max_length=30)
    # objects = TripManager()
    date = models.DateField()
    traveler = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)