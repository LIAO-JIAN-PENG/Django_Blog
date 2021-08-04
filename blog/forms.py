from django.forms.widgets import Widget
from .models import Post, Profile
from django import forms

# form for post
class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Post
        fields = ["title", "author", "content"]


# form for profile
class ProfileForm(forms.ModelForm):
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Profile
        fields = ["user", "description"]
