from django.urls import path
from .views import ListProfile, DetailProfile

app_name = 'profile'

urlpatterns = [
    path('', ListProfile.as_view(), name='list_profile'),
    path('id<int:pk>/', DetailProfile.as_view(), name='detail_profile'),
]
