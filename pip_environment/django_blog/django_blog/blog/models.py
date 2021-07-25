from django.db import models
from django.contrib.auth.models import User

# status for post
STATUS = ((0, "Draft"), (1, "Publish"))

# Create your models here.

# model for profile
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return str(self.user)


# model for post
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title
