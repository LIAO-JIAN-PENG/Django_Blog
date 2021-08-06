from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


# views for post
class PostListView(ListView):
    template_name = "post/post_list.html"
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = "post/post_create.html"
    form_class = PostForm
    queryset = Post.objects.all()

    # check if the form is valid
    def form_valid(self, form):
        # get the current user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    template_name = "post/post_detail.html"
    queryset = Post.objects.all()
