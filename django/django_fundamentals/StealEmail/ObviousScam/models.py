from django.db import models
import re

# Create your models here.
class SuckerManager(models.Manager):
    def SuckerValidator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "We really want your money, so please use your real email"
        if len(postData['password']) < 8:
            errors['password'] = "I think most sites require at least 8 characters"
        return errors



class Sucker(models.Model):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SuckerManager()
