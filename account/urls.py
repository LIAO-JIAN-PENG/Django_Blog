from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include
from .views import (
    UserProfileView,
    UserRegisterView,
    UserEditView,
    UserPasswordChangeView,
    password_success,
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("", include("django.contrib.auth.urls"), name="login"),
    path("edit_profile/", UserEditView.as_view(), name="edit-profile"),
    path("<int:pk>/profile/", UserProfileView.as_view(), name="user-profile"),
    path(
        "password/",
        UserPasswordChangeView.as_view(),
        name="change-password",
    ),
    path("password_success/", password_success, name="password-success"),
]
