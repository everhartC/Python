from django.db import models

# Create your models here.
class CommentManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['content']) < 5:
            errors['content'] = "Comment must be at least 5 characters"
        return errors

class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Name should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Description should be at least 15 characters"
        return errors

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Description: {self.description}"

class Courses(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.OneToOneField(Description, related_name="course", null=True, on_delete=models.CASCADE)
    objects = CourseManager()

    def __repr__(self):
        return f"Course: {self.name}"

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Courses, related_name="has_comments", on_delete=models.CASCADE)
    objects = CommentManager()

    def __repr__(self):
        return f"Comment: {self.content}"
    
    

