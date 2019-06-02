from django.views.generic import ListView
from django.views.generic import View
from django.shortcuts import render, redirect
from src.models.announcement.models import Announcement
from django.views.generic.detail import DetailView



class CreateAnnouncement(View):

    def get(self, request, *args, **kwargs):
        #form = CreateForm()
        return render(request, 'announcement/create.html', {})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return redirect('home:announcement:announcement_list')

class ListAnnouncement(ListView):
    queryset        = Announcement.objects.all()
    template_name   = 'announcement/index.html'



class DetailView(DetailView):
    queryset        = Announcement.objects.all()
    template_name   = 'announcement/detail.html'
