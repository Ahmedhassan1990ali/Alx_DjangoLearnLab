from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})    
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={'pk': self.pk,'post_id': self.post.id})    
    
    def __str__(self):
        return self.content[:50]