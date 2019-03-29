from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from programme.models import Mesure, Avis
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200, verbose_name = 'question')
    pub_date = models.DateField(default = timezone.now(), verbose_name ='date published')
    voters = models.ManyToManyField(User, through = 'Vote')

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    has_voted = models.BooleanField(default = False)

    class Meta:
        unique_together = ("user","question")


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

@receiver(post_save, sender = Question)
def nouvelle_question(sender, instance, **kwargs):
    users = User.objects.all()
    for user in users:
        v = Vote.objects.get_or_create(question = instance, user = user)

@receiver(post_save, sender = User)
def nouveau_utilisateur(sender, instance, **kwrags):
    questions = Question.objects.all()
    mesures = Mesure.objects.all()
    for question in questions:
        v = Vote.objects.get_or_create(question = question, user = instance)
    for mesure in mesures:
        n = Avis.objects.get_or_create(mesure = mesure, user = instance)
