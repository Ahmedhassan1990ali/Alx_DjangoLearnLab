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
from accounts.views import (LoginAPIView, RegisterAPIView, ProfileAPIView,
                            FollowAPIView, UnFollowAPIView,
)


urlpatterns = [
    #path('accounts/',include('accounts.urls')),
    path('register/',RegisterAPIView.as_view(),name="register_api"),
    path('login/',LoginAPIView.as_view(),name='login_api'),
    path('profile/',ProfileAPIView.as_view(),name='profile_api'),
    path('follow/<int:user_id>/',FollowAPIView.as_view(),name='follow_api'),
    path('unfollow/<int:user_id>/',UnFollowAPIView.as_view(),name='unfollow_api'),
]