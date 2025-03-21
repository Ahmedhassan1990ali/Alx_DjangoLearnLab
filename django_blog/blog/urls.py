"""
URL configuration for django_blog project.

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
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from blog.views import (register,profile,home,
                PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
                PostCommentsDetailView, CommentDetailView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path("login/",LoginView.as_view(template_name="blog/login.html"),name="login"),
    path("logout/",LogoutView.as_view(template_name="blog/logout.html"),name="logout"),
    path("register/",register,name="register"),
    path("profile/",profile,name="profile"),
    path('', home,name="home"),
    # Post-related paths
    path('blogposts/', PostListView.as_view(),name="posts"),
    path('posts/',PostListView.as_view(), name="post_list"),
    #path('post/<int:pk>/',PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/',PostCommentsDetailView.as_view(), name="post_detail"),
    path('post/new/',PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name="post_delete"),
    # Comment-related paths
    path('post/<int:post_id>/comment/<int:pk>/',CommentDetailView.as_view(), name="comment_detail"),
    path('post/<int:post_id>/comment/<int:pk>/update/',CommentUpdateView.as_view(), name="comment_update"),
    path('post/<int:post_id>/comment/<int:pk>/delete/',CommentDeleteView.as_view(), name="comment_delete"),
]