from .models import Post, Profile
from django import forms

# form for post
class PostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title", widget=forms.TextInput(attrs={"placeholder": "Your Title"})
    )

    class Meta:
        model = Post
        fields = ["title", "author", "content"]


# form for profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["user", "description"]
