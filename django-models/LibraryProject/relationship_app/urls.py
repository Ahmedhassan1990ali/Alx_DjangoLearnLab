from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('booklist/', list_books, name='booklist'),
    path('library/', LibraryDetailView.as_view(), name='library')
]