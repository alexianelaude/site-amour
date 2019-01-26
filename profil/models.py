from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    highscore = models.IntegerField(default = 0)

