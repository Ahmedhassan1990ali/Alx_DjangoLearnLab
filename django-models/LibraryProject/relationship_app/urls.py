from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    path('booklist/', book_list, name='booklist')
    path('library/', LibraryDetailView.as_view(), name='library')
]