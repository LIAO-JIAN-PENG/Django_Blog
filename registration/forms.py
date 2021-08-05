from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

#  form for registration
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # add some bootstrap magic to fields
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


# form for editing profile
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_login = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "readonly": True}),
    )
    is_superuser = forms.CharField(
        max_length=100,
        widget=forms.CheckboxInput(attrs={"class": "form-check", "readonly": True}),
    )
    is_staff = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={"class": "form-check"})
    )
    is_active = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={"class": "form-check"})
    )
    date_joined = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "readonly": True}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
        ]

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # disable some checkbox
        self.fields["is_superuser"].disabled = True
