from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from myapp.forms import SignupForm,UserEditProfile
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')


def user_signup(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Account Created Successfully...!!!")
            return HttpResponseRedirect("/signup/")
    else:
        fm=SignupForm()
    return render(request,'myapp/signup.html',{"form":fm})
    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                un=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=un,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in successfully..!!!")
                    return HttpResponseRedirect("/profile/")         
        else:
            fm=AuthenticationForm()
        return render(request,'myapp/login.html',{"form":fm})
    
    else:
        return HttpResponseRedirect("/profile/")



def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=UserEditProfile(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'profile updated successfully...!!!')
                return HttpResponseRedirect('/profile/')
        else:
            fm=UserEditProfile(instance=request.user)
        return render(request,"myapp/profile.html",{"form":fm,"user":request.user})
    else:
        return HttpResponseRedirect("/login/")



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect("/login/")



def change_password(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request," your password has been changed successfully...!!")
                return HttpResponseRedirect("/profile/")
        else:       
            fm=PasswordChangeForm(user=request.user)
        return render(request,'myapp/passchange.html',{"form":fm})
    else:
        return HttpResponseRedirect("/login/")



def set_password(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"your New Password has been set successfully...!!")
                return HttpResponseRedirect("/profile/")
        else:       
            fm=SetPasswordForm(user=request.user)
        return render(request,'myapp/setpass.html',{"form":fm})
    else:
        return HttpResponseRedirect("/login/")