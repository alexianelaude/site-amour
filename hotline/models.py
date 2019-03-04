from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# Create your models here.
class Hotline(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_time = models.DateTimeField(auto_now_add = True)
    delivery_time = models.TimeField()
    delivery_date = models.DateField(default = timezone.now())
    delivery_place = models.CharField(max_length = 500)
    comment = models.TextField(null = True, blank = True)


    class Meta:
        abstract = True

class Crepes(Hotline):
    quantity = models.IntegerField()
    garniture = models.CharField(max_length = 300)

class Apero(Hotline):
    quantity = models.IntegerField()
    avec_alcool = models.BooleanField()

class Meme(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_date = models.DateField(auto_now_add = True)
    comment = models.TextField(null = True, blank = True)
