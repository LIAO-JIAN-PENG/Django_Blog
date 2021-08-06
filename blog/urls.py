from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # home page
    path("", RedirectView.as_view(url="post/"), name="home"),
    # urls for post
    path("post/", include("post.urls"), name="post"),
    # urls for memeber
    path("account/", include("account.urls"), name="account"),
]
