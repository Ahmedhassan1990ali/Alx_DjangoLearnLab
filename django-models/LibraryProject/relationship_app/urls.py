"""
URL configuration for LibraryProject project.

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
from django.contrib.auth.views import LoginView
from .views import list_books, LibraryDetailView, LogoutView

from . import views


urlpatterns = [
    path('booklist/', list_books, name='booklist'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path("signup/", views.register, name="register"),
    path('admin/', views.admin_view, name="adminview"),
    path('librarian/', views.librarian_view, name="librarianview"),
    path('member/', views.member_view, name='memberview'),
    path('add_book/',views.add_book, name='add_book'),
    path('edit_book/',views.edit_book, name='edit_book'),
    path('delete_book/',views.delete_book, name='delete_book')

]