from django import forms
from django.contrib.auth.models import User
from blog.models import Post

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","content"]