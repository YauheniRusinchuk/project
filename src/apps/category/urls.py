from django.urls import path
from .views import CategoryPartnerView, CategoryIdeas, CategoryJobs

app_name = 'category'

urlpatterns = [
    path('search-partner/', CategoryPartnerView.as_view(), name='partner_page'),
    path('ideas/', CategoryIdeas.as_view(), name='ideas_page'),
    path('jobs/', CategoryJobs.as_view(), name='jobs_page'),
]
