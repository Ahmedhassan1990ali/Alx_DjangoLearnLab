from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context ={"books":books}
    return render(request, "relationship_app/list_books.html",context)

class Library(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
