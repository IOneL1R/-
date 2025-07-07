from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



def profile(request):
    user = User.objects.filter(is_superuser=True).first()
    profile = Profile.objects.get(user = user)
    return render(request,"users/profile.html",{"profile":profile,"user":user})

def auth1(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request,"users/register.html",{"form":form})








