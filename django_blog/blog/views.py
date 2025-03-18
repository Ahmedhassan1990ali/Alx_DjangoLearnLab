from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

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

def profile(request):
    return render(request,"blog/profile.html")