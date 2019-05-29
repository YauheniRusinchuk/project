from django.views.generic import ListView
from src.models.announcement.models import Announcement
from django.views.generic.detail import DetailView


class ListAnnouncement(ListView):
    queryset        = Announcement.objects.all()
    template_name   = 'announcement/index.html'



class DetailView(DetailView):
    queryset        = Announcement.objects.all()
    template_name   = 'announcement/detail.html'
