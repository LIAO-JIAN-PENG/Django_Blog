from .models import Profile
from django import forms


# form for profile
class ProfileForm(forms.ModelForm):
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Profile
        fields = ["description"]
