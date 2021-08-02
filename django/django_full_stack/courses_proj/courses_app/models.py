from django.db import models

# Create your models here.
class ErrorManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Course name should be more than 5 characters'
        if len(postData['desc']) < 10:
            errors['desc'] = 'Description needs to be greater than 10 characters'
        return errors


class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ErrorManager()

    def __repr__(self):
        return f"Description: {self.content}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.OneToOneField(Description, related_name="course", on_delete=models.CASCADE, null=True)
    objects = ErrorManager()

    def __repr__(self):
        return f"Course: {self.name}"

