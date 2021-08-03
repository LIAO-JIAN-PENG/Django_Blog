from django.urls import path
from .views import (
    PostCreateView,
    PostDetailView,
    PostListView,
    ProfileUpdateView,
    ProfileDetailView,
)

urlpatterns = [
    # urls for post
    path("", PostListView.as_view(), name="post_list"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    # urls for profile
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path(
        "profile/<int:pk>/update/", ProfileUpdateView.as_view(), name="profile_update"
    ),
]
