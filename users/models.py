from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ava = models.ImageField(upload_to='ava/', blank=True)
    des = models.TextField(blank=True)
