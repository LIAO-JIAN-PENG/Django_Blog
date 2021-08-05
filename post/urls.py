from .views import PostCreateView, PostDetailView, PostListView, LikeView
from django.urls import path

urlpatterns = [
    # urls for post
    path("", PostListView.as_view(), name="post_list"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path('like/<int:pk>', LikeView, name="like_post"),
]
