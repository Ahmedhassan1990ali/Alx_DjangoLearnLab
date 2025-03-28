from rest_framework import serializers
from posts.models import Post, Comment
from accounts.models import CustomUser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","author","title","content","created_at","updated_at"]
        read_only_fields = ["id","author","created_at","updated_at"]



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id","post","author","content","created_at","updated_at"]
        read_only_fields = ["id","author","created_at","updated_at"]

    


