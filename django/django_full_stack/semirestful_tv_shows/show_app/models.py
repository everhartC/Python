from django.db import models
from datetime import datetime, date


# Create your models here.
class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors['desc'] = "Description needs to be at least 10 characters"
        if datetime.strptime(postData['reldate'], '%Y-%m-%d') > datetime.today():          # Rel Date should be in the past
            errors['reldate'] = "Release Date must be in the past (i.e. not today or in the future)"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"{self.network}: {self.title}"


