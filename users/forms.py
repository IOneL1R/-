from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile

class CustomUserCreationForm(UserCreationForm):
    ava = forms.ImageField(required=False,label="anatar")
    emeil = forms.EmailField(required=True,help_text="Введи ваш emeil")

    class Meta:
        model = User
        fields = ["Username", "emeil","ava","passworld1", "passworld2"]