from django.shortcuts import render, redirect,  get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
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
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})

###########################################

@permission_required("relationship_app.can_add_book")
def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST["title"], 
            author=request.POST["author"]
        )
        return redirect("add_book")
    return render(request, "relationship_app/add_book.html")

@permission_required("relationship_app.can_change_book")
def edit_book(request, b_title):
    book = get_object_or_404(Book, title=b_title)
    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.save()
        return redirect("edit_book")
    return render(request, "relationship_app/edit_book.html", {"book": book})

@permission_required("relationship_app.can_delete_book")
def delete_book(request, b_title):
    book = get_object_or_404(Book, title=b_title)
    if request.method == "POST":
        book.delete()
        return redirect("home")
    return render(request, "relationship_app/delete_book.html", {"book": book})


##########################################
from django.contrib.auth import logout

def logoutview(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

###########################################
from django.views import View
class LogoutView(View):
    template_name = ""
    def get(self, request):
        """Handles logout via GET request."""
        logout(request)  # Logs out the user
        return render(request, self.template_name)  # Show a logout page

    #def post(self, request):
    #    """Handles logout via POST request."""
    #    logout(request)
    #    return redirect('/login/')  # Redirect to login after logout

