from django.shortcuts import render
from django.views.generic import DetailView
from . import models

# Create your views here.

def book_list(request):
    books = models.Book.objects.all()
    context ={"books":books}
    return render(request, "relationship_app/list_books.html",context)

class Library(DetailView):
    model = models.Library
    template_name = "relationship_app/library_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
