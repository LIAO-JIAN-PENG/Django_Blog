from django.contrib.auth.views import PasswordChangeView
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from .forms import AccountSettingForm, ChangePasswordForm, EditProfileForm, SignUpForm
from .models import Profile


# views for member
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserAccountSettingView(UpdateView):
    form_class = AccountSettingForm
    template_name = "registration/account_setting.html"
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


    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        profile = get_object_or_404(Profile, id=self.kwargs["pk"])
        default_image = "/media/images/post/default.png"
        context["profile"] = profile
        context["default"] = default_image

        return context


class UserEditProfileView(UpdateView):
    form_class = EditProfileForm
    model = Profile
    template_name = "registration/edit_profile.html"

    def get_success_url(self):
        pk = self.request.user.profile.pk
        return reverse_lazy("user-profile", args=[str(pk)])
