from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserRegisterForm


# user login view
class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, "registration/login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            # Check the user to see if the information is correct
            if user != None:
                login(request, user)
                messages.success(request, "you are logged in")
                return redirect("/")
            else:
                messages.error(
                    request, "you are not logged in , check your information"
                )
                return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, "you are not logged in , check your information")
            return redirect("user:login")


# user register view
class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, "registration/signup.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd["username"], email=cd["email"], password=cd["password1"]
            )
            login(request, user)
            messages.success(request, "your account is created and you are logged in")
            return redirect("/")


# user logout view
class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "you are logged out")
        return redirect("/")
