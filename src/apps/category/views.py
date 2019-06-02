from django.views.generic.list import ListView
from src.models.announcement.models import Announcement


class CategoryPartnerView(ListView):
    queryset        = Announcement.objects.filter(category=1)
    template_name   = 'announcement/index.html'



class CategoryIdeas(ListView):
    queryset        = Announcement.objects.filter(category=2)
    template_name   = 'announcement/index.html'



class CategoryJobs(ListView):
    queryset        = Announcement.objects.filter(category=3)
    template_name   = 'announcement/index.html'
