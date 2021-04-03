from django.db import models
from login.models import *


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title'] = "You can't leave title empty"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    def __repr__(self):
        return f"Title: {self.title}, Uploaded By: {self.uploaded_by}"


class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewer = models.ForeignKey(User, related_name="written_reviews", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)

    def __repr__(self):
        return f"Review: {self.comment}, Rating: {self.rating}"

