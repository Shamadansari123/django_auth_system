from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("signup/",views.user_signup,name="signup"),
    path("login/",views.user_login,name="login"),
    path("profile/",views.user_profile,name="profile"),
    path("logout/",views.user_logout,name="logout"),
    path("passchange",views.change_password,name="passchange"),
    path("setpass/",views.set_password,name="setpass"),
]
