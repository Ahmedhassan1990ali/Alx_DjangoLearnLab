from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

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