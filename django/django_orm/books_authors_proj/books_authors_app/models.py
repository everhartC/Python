from django.db import models

# Create your models here.
class Authors(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Authors Object: {self.fname} {self.lname}"

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    authors = models.ManyToManyField(Authors, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Books object: {self.title}"



