from django.urls import path
from .views import ListAnnouncement

app_name = 'accouncement'

urlpatterns = [
    path('', ListAnnouncement.as_view(), name='accouncement_list'),
]
