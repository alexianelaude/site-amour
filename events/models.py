from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 300)
    slug = models.SlugField(max_length = 50)
    debut = models.DateTimeField(default = timezone.now)
    fin = models.DateTimeField(default = timezone.now)
    gallerie = models.FilePathField(path = 'static/', null = True, blank = True, allow_folders = True)
    description = models.TextField(blank = True, null = True)
