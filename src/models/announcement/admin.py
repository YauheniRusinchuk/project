from django.contrib import admin
from .models import Announcement, CategoryPost

admin.site.register(CategoryPost)
admin.site.register(Announcement)
