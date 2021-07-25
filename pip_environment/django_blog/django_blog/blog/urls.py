from django.urls import path
from .views import PostListView, ProfileDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
]
