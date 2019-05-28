from django.views.generic import ListView
from django.views.generic.detail import DetailView
from src.models.profile.models import Profile


class ListProfile(ListView):
    model           = Profile
    template_name   = 'profile/index.html'


class DetailProfile(DetailView):
    model           = Profile
    template_name   = 'profile/detail.html'
