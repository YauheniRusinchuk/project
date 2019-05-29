from django.db import models
from src.models.profile.models import Profile

class Announcement(models.Model):

    author  = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title   = models.CharField(max_length=300, blank=False)
    text    = models.TextField(blank=True)


    def __str__(self):
        return f"{self.title}"
