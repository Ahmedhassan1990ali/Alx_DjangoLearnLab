from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase, GenericTaggedItemBase

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.name
    
class CustomTaggedItem(GenericTaggedItemBase, TaggedItemBase): 
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="taggit_items")


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    taggit_tags = TaggableManager(through=CustomTaggedItem, blank=True)

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
        return reverse('comment_detail', kwargs={'post_id': self.post.pk, 'pk': self.pk})
    
    def __str__(self):
        return self.content[:50]
    


