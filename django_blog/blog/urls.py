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
from blog.views import register,profile

urlpatterns = [
    path("login/",LoginView.as_view(template_name="blog/login.html"),name="login"),
    path("logout/",LogoutView.as_view(template_name="blog/logout.html"),name="logout"),
    path("register/",register,name="register"),
    path("profile/",profile,name="profile"),
    path('a/', profile,name="home"),
    path('b/', profile,name="posts"),
]