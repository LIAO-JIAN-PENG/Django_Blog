from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm, EditProfileForm
from django.urls import reverse_lazy

# views for user
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
