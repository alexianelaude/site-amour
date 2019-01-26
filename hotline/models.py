from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotline(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order = models.CharField(max_length = 300)
    order_time = models.DateTimeField(auto_now_add = True)
    delivery_time = models.DateTimeField()
    delivery_place = models.CharField(max_length = 500)
    comment = models.TextField()

