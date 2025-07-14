from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

@login_required
def profile(request):
    user = request.user
    profile = user.profile
    return render(request,"users/profile.html",{"profile":profile,"user":user})

def auth1(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user = user)

            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request,"users/register.html",{"form":form})







