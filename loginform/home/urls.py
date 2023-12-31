
from django.urls import path
from .import views


urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.user_login, name="login"),
    path('signup',views.user_signup, name="signup"),
    path('home/',views.home, name="home"),
    path('home/logout',views.user_logout, name="logout"),
]
