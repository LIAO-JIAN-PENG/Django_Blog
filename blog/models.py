from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

# status for post
STATUS = ((0, "Draft"), (1, "Publish"))

# model for profile
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return str(self.user)

    # return to detail page
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.id})


# model for post
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
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

    # create slug for post
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(args, kwargs)

    # return to detail page
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


# model for member
