from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from posts.forms import PostCreateForm

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



@login_required  # Если нужно, чтобы только авторизованные пользователи могли создавать посты
def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Если у модели Post есть поле author
            post.save()
            return redirect('post_detail', pk=post.pk)  # Перенаправляем на страницу поста
    else:
        form = PostCreateForm()
    
    return render(request, 'posts/create_post.html', {'form': form})







