from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Library, Book





# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context ={"books":books}
    return render(request, "relationship_app/list_books.html",context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
"""
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def register(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get authenticated user
            login(request, user)  # Log in the user
            return redirect("home")  # Redirect after login
    else:
        form = AuthenticationForm()

    return render(request, "registeration/login.html", {"form": form})
"""


# ✅ User Registration View    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log in the new user
            return redirect("home")  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

# ✅ User Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home page
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

# ✅ User Logout View
@login_required
def logout_view(request):
    logout(request)
    return render(request, "accounts/logout.html")