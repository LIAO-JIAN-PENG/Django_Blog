from django.urls import path, include
from django.views.generic import RedirectView

from .views import (
    ProfileUpdateView,
    ProfileDetailView,
)

urlpatterns = [
    path("", RedirectView.as_view(url="post/"), name="home"),
    # urls for post
    path("post/", include("post.urls"), name="post"),
    # urls for profile
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path(
        "profile/<int:pk>/update/", ProfileUpdateView.as_view(), name="profile_update"
    ),
    # urls for memeber
    path("account/", include("registration.urls"), name="account"),
]
