from django.shortcuts import render
from .models import Topic
# Create your views here.



def topic_detail(request):
    # topic = {
    #     "title": "Добро пожаловать",
    #     "description": "Пепвая тема форума"  #  Напиши краткое описание темы
    # }
    topic = Topic.objects.all()
    #  Верни шаблон topic_detail.html и передай туда topic и posts
    return render(request,'posts/topic_detail.html', {"topic": topic} )
