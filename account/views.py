from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import ChangePasswordForm, SignUpForm, EditProfileForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.views import PasswordChangeView

# views for member
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("password-success")


def password_success(request):
    return render(request, "registration/password_success.html", {})


class UserProfileView(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"
    queryset = Profile.objects.all()
