from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(LoginRequiredMixin,generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(LoginRequiredMixin,generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(LoginRequiredMixin,generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


