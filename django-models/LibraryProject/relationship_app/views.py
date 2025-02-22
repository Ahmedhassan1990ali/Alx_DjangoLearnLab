from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
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


# User Registration View    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log in the new user
            return redirect("home")  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

########################################
def is_admin(user):
    return user.is_authenticated and getattr(user, 'userprofile', None) and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and getattr(user, 'userprofile', None) and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and getattr(user, 'userprofile', None) and user.userprofile.role == 'Member' 

@user_passes_test(is_admin)
def Admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

@user_passes_test(is_librarian)
def Librarian(request):
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})

@user_passes_test(is_member)
def Member(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})



from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

class AdminView(UserPassesTestMixin, TemplateView):
    template_name = "admin_view.html"
    login_url = "/custom-login/"  # Optional custom redirect

    def test_func(self):
        return hasattr(self.request.user, "userprofile") and self.request.user.userprofile.role == "Admin"
    
class Admin(UserPassesTestMixin, TemplateView):
    template_name = "admin_view.html"
    login_url = "/custom-login/"  # Optional custom redirect

    def test_func(self):
        return hasattr(self.request.user, "userprofile") and self.request.user.userprofile.role == "Admin"
    
class Admin_View(UserPassesTestMixin, TemplateView):
    template_name = "admin_view.html"
    login_url = "/custom-login/"  # Optional custom redirect

    def test_func(self):
        return hasattr(self.request.user, "userprofile") and self.request.user.userprofile.role == "Admin"
    
class admin_view(UserPassesTestMixin, TemplateView):
    template_name = "admin_view.html"
    login_url = "/custom-login/"  # Optional custom redirect

    def test_func(self):
        return hasattr(self.request.user, "userprofile") and self.request.user.userprofile.role == "Admin"

class admin(UserPassesTestMixin, TemplateView):
    template_name = "admin_view.html"
    login_url = "/custom-login/"  # Optional custom redirect

    def test_func(self):
        return hasattr(self.request.user, "userprofile") and self.request.user.userprofile.role == "Admin"