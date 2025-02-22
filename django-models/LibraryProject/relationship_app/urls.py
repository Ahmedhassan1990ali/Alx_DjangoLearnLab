from django.urls import path
from . import views

urlpatterns = [
    path('booklist/', views.book_list, name='booklist')
    path('library/', views.Library.as_view(), name='library')
]