from django.shortcuts import render
from posts.models import Post,Comment
from posts.serializers import PostSerializer, CommentSerializer
from posts.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommenyViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)