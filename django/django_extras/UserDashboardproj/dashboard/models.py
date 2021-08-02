from django.db import models
from login.models import User
# Create your models here.


class Message(models.Model):
    msg = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Message: {self.msg} by {self.user}"


class Comment(models.Model):
    cmt = models.TextField()
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    msg = models.ForeignKey(Message, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Comment: {self.cmt} by {self.user}"