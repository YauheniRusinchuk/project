from django.urls import path
from .views import ListAnnouncement, DetailView, CreateAnnouncement

app_name = 'announcement'

urlpatterns = [
    path('create/', CreateAnnouncement.as_view(), name='announcement_create'),
    path('article<int:pk>/', DetailView.as_view(), name='announcement_detail'),
    path('', ListAnnouncement.as_view(), name='announcement_list'),
]
