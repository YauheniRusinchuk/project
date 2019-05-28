from django.urls import path
from .views import RegisterView

app_name = 'register_page'

urlpatterns = [
    path('', RegisterView.as_view(), name='new_user'),
]
