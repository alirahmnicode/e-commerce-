from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from .models import Profile

from order.models import Order


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
                username=cd["username"], password=cd["password1"]
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


class DashboardView(View):
    def get(self, request, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
            form = UserProfileForm(instance=profile)
        except:
            profile = None
            form = UserProfileForm
        orders = Order.objects.filter(user_info=profile)
        return render(
            request,
            "registration/dashboard.html",
            {"form": form, "profile": profile, "orders": orders},
        )


def create_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "your profile is created")
        else:
            messages.error(request, "check informations,your profile is not created")
        return redirect(request.META.get("HTTP_REFERER"))


def edit_profile(request, pk):
    if request.method == "POST":
        instance = get_object_or_404(Profile, pk=pk)
        form = UserProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "your profile is updated")
        else:
            messages.error(request, "check informations,your profile is not updated")
        return redirect(request.META.get("HTTP_REFERER"))
