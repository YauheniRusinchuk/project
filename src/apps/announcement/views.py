from django.views.generic import ListView
from django.views.generic.edit import CreateView
from src.models.announcement.models import Announcement
from django.views.generic.detail import DetailView


class CreateAnnouncement(CreateView):
    model = Announcement
    template_name = 'announcement/create.html'
    fields = '__all__'


class ListAnnouncement(ListView):
    queryset        = Announcement.objects.all()
    template_name   = 'announcement/index.html'



class DetailView(DetailView):
    queryset        = Announcement.objects.all()
    template_name   = 'announcement/detail.html'
