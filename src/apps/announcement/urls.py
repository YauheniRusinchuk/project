from django.urls import path
from .views import ListAnnouncement, DetailView

app_name = 'announcement'

urlpatterns = [
    path('article<int:pk>/', DetailView.as_view(), name='announcement_detail'),
    path('', ListAnnouncement.as_view(), name='announcement_list'),
]
