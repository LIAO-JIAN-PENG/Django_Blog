from .models import Post
from django import forms
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget


# form for post
class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    content = forms.CharField(widget=CKEditorWidget())
    image = forms.ImageField(
        label=_("post_image"),
        required=False,
        error_messages={"invalid": _("Image files only")},
    )

    class Meta:
        model = Post
        fields = ["title", "content", "image"]
