from .views import PostCreateView, PostDetailView, PostListView, LikeView
from django.urls import path

urlpatterns = [
    # urls for post
    path("", PostListView.as_view(), name="post-list"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("like/<int:pk>", LikeView, name="like-post"),
]
