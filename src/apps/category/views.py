from django.views.generic.list import ListView
from src.models.announcement.models import Announcement


class CategoryPartnerView(ListView):
    queryset        = Announcement.objects.filter(type='поиск')
    template_name   = 'announcement/index.html'



class CategoryIdeas(ListView):
    queryset        = Announcement.objects.filter(type='идеи')
    template_name   = 'announcement/index.html'



class CategoryJobs(ListView):
    queryset        = Announcement.objects.filter(type='работа')
    template_name   = 'announcement/index.html'
