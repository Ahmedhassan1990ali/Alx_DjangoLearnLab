from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post,Comment
from posts.serializers import PostSerializer, CommentSerializer
from posts.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['post', 'author']
    search_fields = ['content'] 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)