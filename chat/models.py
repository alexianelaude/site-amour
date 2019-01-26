from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    message = models.CharField(max_length = 300, verbose_name = 'message')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(default = timezone.now)