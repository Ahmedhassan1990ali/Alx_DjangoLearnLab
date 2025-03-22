from django import forms
from django.contrib.auth.models import User
from blog.models import Post, Comment
from taggit.forms import TagWidget

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email"]

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas",
        widget=TagWidget()#attrs={'placeholder': 'e.g. django, python, web'}
    )
    class Meta:
        model = Post
        fields = ["title","content"]
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your post content here...'}),
        }
    def clean_tags(self):
        tags = self.cleaned_data.get('tags', '')
        return [tag.strip() for tag in tags.split(',') if tag.strip()]
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]