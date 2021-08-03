from .forms import PostForm, ProfileForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Profile, Post


# views for post
class PostListView(ListView):
    template_name = "post/post_list.html"
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = "post/post_create.html"
    form_class = PostForm
    queryset = Post.objects.all()
    # success_url = "../"

    # check if the form is valid
    def form_valid(self, form):
        return super().form_valid(form)


class PostDetailView(DetailView):
    template_name = "post/post_detail.html"
    queryset = Post.objects.all()


# views for profile
class ProfileDetailView(DetailView):
    template_name = "profile/profile_detail.html"
    queryset = Profile.objects.all()


class ProfileUpdateView(UpdateView):
    template_name = "profile/profile_update.html"
    form_class = ProfileForm
    queryset = Profile.objects.all()

    # check if the form is valid
    def form_invalid(self, form):
        return super().form_invalid(form)
