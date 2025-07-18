from django.urls import path
from . import views
from django.contrib.auth import views as auth_v


urlpatterns = [
    path("profile/",  views.profile , name="profile"),
    path('register/',views.auth1, name="reg"),
    path('login/', auth_v.LoginView.as_view(template_name = "users/login.html",
                                            redirect_authenticated_user=True,
                                            next_page='/profile/profile/'
                                            ), name="login"),
    path('logout/',auth_v.LogoutView.as_view(next_page="/"), name="logout"),
    path('create/', views.create_post, name='create_post'),
    
    
]