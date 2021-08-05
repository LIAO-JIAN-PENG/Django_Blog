from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# model for profile
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return str(self.user)

    # return to detail page
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.id})
