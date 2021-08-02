from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=200)
    network = models.CharField(max_length=40)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.title} on {self.network}"