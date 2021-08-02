from django.db import models
from django.core.exceptions import ValidationError
import re
import bcrypt


# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        # Checks to see that First and Last name are greater than 2 characters
        if len(postData['first_name']) < 2:
            errors['first_name'] = "There needs to be at least 2 characters, letters only"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "There needs to be at least 2 characters, letters only"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confpw']:
            errors['password'] = "Passwords don't match. Please try again."

        same_email = self.filter(email=postData['email'])
        if same_email:
            errors['email'] = "Email is already in use"

        # Go here to test regex https://regex101.com/
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("invalid email")
        return errors

    def authenticate(self, email, password):
        all_users = User.objects.filter(email=email)
        # If the email doesn't match one of the emails on the server
        # return False
        if not all_users:
            return False

        # If it does match, make user = all_users[0] 
        # since all_users should be a list of 1
        user = all_users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, postData):
        # Concatenate the password in the form with a generated salt
        pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        # Since register is models objects its "self" has django attributes
        # return a self.create object
        return self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = pw, # only sends the hashed version of pw to server
        )

    def capnames(self):
        return self.fname.capitalize(), self.lname.capitalize()

class PostManager(models.Manager):
    def validate_content(value):
        if len(value) < 10:
            raise ValidationError(
                f"{value} must be longer than 10 characters."
            )


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"


class Post(models.Model):
    content = models.TextField(validators=[PostManager.validate_content])
    poster = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)