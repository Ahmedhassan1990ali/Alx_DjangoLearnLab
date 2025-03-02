from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
# Create your views here.


@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request):
    context = { "book_list" : Book.objects.aLL() }
    return render(request, "bookshelf/edit.html", context)