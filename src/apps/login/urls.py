from django.urls import path
from .views import LoginView

app_name = 'login_page'

urlpatterns = [
    path('', LoginView.as_view(), name='check_login'),
]
