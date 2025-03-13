from django.shortcuts import render
from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
import django_filters
 
# Create your views here.

class BookFilter(django_filters.FilterSet):
    title = django_filters.Charfilter(lookup_expr='icontains')
    author = django_filters.Charfilter(lookup_expr='icontains')
    publication_year = django_filters.Numderfilter(lookup_expr='exact')
    publication_year__gte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='gte')
    publication_year__lte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lte')
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title','author','publication_year']
    ordering_fields = ['title','author','publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


