from django.views.generic import ListView
from src.models.announcement.models import Announcement


class ListAnnouncement(ListView):
    queryset        = Announcement.objects.all()
    template_name   = 'announcement/index.html'
