from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from blog.forms import ProfileUpdateForm, PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from django.urls import reverse_lazy


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"blog/profile.html")
        return render(request,"blog/register.html",{"form":form})
    form = UserCreationForm()
    return render(request,"blog/register.html",{"form":form})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
        return redirect("profile")
    form = ProfileUpdateForm(instance=request.user)
    return render(request,"blog/profile.html",{"form":form})

def home(request):
    user_name = request.user.username
    return render(request, "blog/home.html",{"user":user_name})

class PostListView(ListView):
    template_name = "blog/post_list.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-published_date"]

class PostDetailView(DetailView):
    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "blog/post_form.html"
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "blog/post_form.html"
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "blog/post_delete.html"
    model = Post
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user



