from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm
# Create your views here.


@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request):
    context = { "book_list" : Book.objects.aLL() }
    return render(request, "bookshelf/edit.html", context)

def example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            return render(request, "bookshelf/success.html", {"name": name})
    else:
        form = ExampleForm()

    return render(request, "bookshelf/example_form.html", {"form": form})