from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Profile, Post

# Create your views here.
class PostListView(ListView):
    template_name = "post/post_list.html"
    queryset = Post.objects.all()


class ProfileDetailView(DetailView):
    template_name = "profile/profile_detail.html"
    queryset = Profile.objects.all()
