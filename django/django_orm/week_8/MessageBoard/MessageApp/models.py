from django.db import models


# Create your models here.
class Message(models.Model):
    author = models.CharField(max_length=60)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    content = models.TextField()
    originalMessage = models.ForeignKey(Message, 
        related_name='all_comments', 
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    