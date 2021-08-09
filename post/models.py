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
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    image = models.ImageField(null=True, blank=True, upload_to="images/post/")
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes")

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title

    # return to detail page
    def get_absolute_url(self):
        # return reverse("post-detail", args=[str(self.pk)])
        return reverse("post-detail", args=[str(self.pk)])
