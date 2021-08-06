from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid

# status for post
STATUS = ((0, "Draft"), (1, "Publish"))


# model for post
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=400, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes")

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title

    # create slug for post
    def save(self, *args, **kwargs):
        self.slug = uuid.uuid4
        super(Post, self).save(*args, **kwargs)

    # return to detail page
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])
