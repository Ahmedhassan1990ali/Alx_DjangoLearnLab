from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from blog.forms import ProfileUpdateForm, PostForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Comment
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


######################################################################################
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

######################################################################################

class PostCommentsDetailView(DetailView):
    model = Post
    template_name = "blog/post_comments.html"
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = kwargs.get("form", CommentForm())
        return context
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated:
                return redirect("login")
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=self.object.pk)
        return render(request, self.template_name, self.get_context_data(form=form))

class CommentDetailView(DetailView):
    model = Comment
    template_name = "blog/comment_detail.html"
    context_object_name = "comment"

class CommentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    template_name = "blog/comment_form.html"
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = "blog/comment_delete.html"
    def get_success_url(self):
        post = self.get_object().post
        return reverse_lazy("post_detail", kwargs={"pk": post.id})
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author