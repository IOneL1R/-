from django.shortcuts import render
from .models import Profile


def profile(request):
    profile = Profile.objects.get(user = "IOneL1R")
    return render(request,"users/profile.html",{"profile":profile})






