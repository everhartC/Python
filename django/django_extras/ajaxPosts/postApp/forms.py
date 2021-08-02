# from django.forms import widgets
# from python.django.django_extras.ajaxPosts.postApp.models import User
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['content']

