from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


# Create your models here.
class Hotline(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_time = models.DateTimeField(auto_now_add = True)
    delivery_time = models.TimeField()
    delivery_date = models.DateField(default = timezone.now)
    delivery_place = models.CharField(max_length = 500)
    comment = models.TextField(null = True, blank = True)
    delivered = models.BooleanField(default = False)


    class Meta:
        abstract = True

class Crepes(Hotline):
    garniture = models.CharField(max_length = 300)

class Apero(Hotline):
    quantity = models.IntegerField(default = 1, validators = [MaxValueValidator(40),MinValueValidator(1)])
    biere = models.IntegerField(default = 0, validators = [MinValueValidator(0)])
    vin = models.IntegerField(default = 0, validators = [MinValueValidator(0)])
    cidre = models.IntegerField(default = 0, validators = [MinValueValidator(0)])
    cocktail = models.IntegerField(default = 0, validators = [MinValueValidator(0)])
    virgin_cocktail = models.IntegerField(default = 0, validators = [MinValueValidator(0)])
    vege = models.IntegerField(default = 0, validators = [MinValueValidator(0)])

class Meme(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_date = models.DateField(auto_now_add = True)
    comment = models.TextField(null = True, blank = True)

class PetitDej(Hotline):
    gout_muffin = models.CharField(max_length = 500)
    compote = models.CharField(max_length = 300)
    quatre_quart = models.BooleanField (default = True)
    boisson_chaude = models.CharField(max_length = 500)
    jus = models.CharField(max_length = 500)
    tartine = models.CharField(max_length = 500)

class Muffin(Hotline):
    gout_muffin = models.CharField(max_length = 500)


