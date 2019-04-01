from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Mesure(models.Model):
    name = models.CharField(max_length = 300)
    preambule = models.TextField(null = True)
    constat = models.TextField(null = True, blank = True)
    concret = models.TextField(null = True, blank = True)


class Avis(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    mesure = models.ForeignKey(Mesure, on_delete = models.CASCADE)
    note = models.IntegerField(null = True, blank = True)
    comment = models.TextField(null = True, blank = True)

class Idee(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField()

@receiver(post_save, sender = Mesure)
def nouvelle_question(sender, instance, **kwargs):
    users = User.objects.all()
    for user in users:
        v = Avis.objects.get_or_create(mesure = instance, user = user)

