from django.urls import path
from .views import (
    UserLoginView,
    UserLogoutView,
    UserRegisterView,
    DashboardView,
    create_profile,
)


app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("signup/", UserRegisterView.as_view(), name="signup"),
    path("dashboard/<str:username>/", DashboardView.as_view(), name="dashboard"),
    path("profile/create/", create_profile, name="profile_create"),
]
