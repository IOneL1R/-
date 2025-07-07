from django.urls import path
from .views import topic_detail
urlpatterns = [
    path("test-topic/", topic_detail, name="topic_detail"),
] 
