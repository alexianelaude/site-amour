from .models import EscapeGame
from django import forms
import datetime
from django.utils import timezone


class EscapeGameForm(forms.Form):
    #quantity = forms.IntegerField(label = 'Combien de personnes souhaites-tu inscrire?', widget = forms.widgets.Select(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4')]))
    time = forms.TimeField(label = 'A quelle heure souhaites-tu inscrire ton équipe?', widget = forms.widgets.Select(choices = [(datetime.time(10,0,0),"10h"),(datetime.time(10,45,0),'10h45'),(datetime.time(11,30,0),"11h30")]))