from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView


app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("signin/", UserRegisterView.as_view(), name="signin"),
]
