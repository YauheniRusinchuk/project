from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    username        = models.CharField(max_length=255)
    description     = models.TextField()



    def __str__(self):
        return f"profile {self.user}"
