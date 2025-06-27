from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    titel = models.CharField(max_length=200)
    des = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    auter = models.ForeignKey(User, on_delete=models.CASCADE)
