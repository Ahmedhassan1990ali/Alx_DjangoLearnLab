"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from posts.views import (PostViewSet, CommentViewSet, FeedAPIView,
                         LikeAPIView, UnlikeAPIView) 

router = DefaultRouter()
router.register(r"posts",PostViewSet)
router.register(r"comments",CommentViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('feed/',FeedAPIView.as_view(),name='feed_api'),
    path('like/<int:post_id>/',LikeAPIView.as_view(),name='like_api'),
    path('unlike/<int:post_id>/',UnlikeAPIView.as_view(),name="unlike_api"),
]