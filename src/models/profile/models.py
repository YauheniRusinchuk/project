from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


User = get_user_model()



class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    username        = models.CharField(max_length=255)
    description     = models.TextField()
    avatar          = models.ImageField(upload_to='avatar/', blank=True)


    def __str__(self):
        return f"profile {self.user}"


    def get_absolute_url(self):
        return reverse('home:profile:detail_profile', kwargs={'pk': self.pk})
