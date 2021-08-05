from .views import PostCreateView, PostDetailView, PostListView
from django.urls import path, include

urlpatterns = [
    # urls for post
    path("", PostListView.as_view(), name="post_list"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]
