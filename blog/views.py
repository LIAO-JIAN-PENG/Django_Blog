from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, UpdateView
from .models import Profile
from .forms import ProfileForm


# views for profile
class ProfileDetailView(DetailView):
    template_name = "profile/profile_detail.html"
    queryset = Profile.objects.all()


class ProfileUpdateView(UpdateView):
    template_name = "profile/profile_update.html"
    form_class = ProfileForm
    queryset = Profile.objects.all()

    # check if the form is valid
    def form_invalid(self, form):
        # get the current user
        form.instance.user = self.request.user
        return super().form_invalid(form)
