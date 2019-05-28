from django.urls import path, include
from .views import index

app_name = 'home'

urlpatterns = [
    path('profiles/', include('src.apps.profile.urls', namespace='profile')),
    path('register/', include('src.apps.register.urls', namespace='register_page')),
    path('exit/', include('src.apps.logout.urls', namespace='exit')),
    path('login/', include('src.apps.login.urls', namespace='login_page')),
    path('', index, name='home_page')
]
