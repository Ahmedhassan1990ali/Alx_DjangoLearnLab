from rest_framework import serializers
from posts.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["author","title","content","created_at","updated_at"]
        read_only_fields = ["created_at","updated_at"]



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post","author","content","created_at","updated_at"]
        read_only_fields = ["created_at","updated_at"]


