from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return render(reverse("post-detail", args=[str(pk)]))


# views for post
class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "post/post_create.html"
    form_class = PostForm

    # check if the form is valid
    def form_valid(self, form):
        # get the current user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs.get("pk"))
        total_likes = stuff.likes.all().count()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
