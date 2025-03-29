from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post, Comment, Like
from posts.serializers import PostSerializer, CommentSerializer
from posts.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, filters, generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.models import Notification


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
        comment = serializer.save(author=self.request.user)
        post = get_object_or_404(Post, id=comment.post.id)
        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb="commented on your post",
                target=comment
            )

class FeedAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        following_users = self.request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
        return posts
    
class LikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, id, post_id):
        user = request.user
        post = get_object_or_404 (Post,id=post_id)
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        Like.objects.create(user=user,post=post)    
        Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target=post
            )
        return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)

class UnlikeAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, post_id):
        user = request.user
        post = get_object_or_404(Post, id=post_id)

        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"message": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"message": "Post unliked."}, status=status.HTTP_204_NO_CONTENT)