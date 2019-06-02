from django.db import models
from src.models.profile.models import Profile
from django.shortcuts import reverse


class Announcement(models.Model):

    author  = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title   = models.CharField(max_length=300, blank=False)
    text    = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return f"{self.title}"


    def get_absolute_url(self):
        return reverse('home:announcement:announcement_detail', kwargs={"pk": self.pk})
