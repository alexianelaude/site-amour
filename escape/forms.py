from .models import EscapeGame
from django import forms
import datetime
from django.utils import timezone


class EscapeGameForm(forms.Form):
    #quantity = forms.IntegerField(label = 'Combien de personnes souhaites-tu inscrire?', widget = forms.widgets.Select(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4')]))
    time = forms.TimeField(label = 'A quelle heure souhaites-tu inscrire ton équipe?', widget = forms.widgets.Select(choices = [(datetime.time(9,0,0),"9h"),(datetime.time(9,45,0),'9h45'),(datetime.time(10,30,0),"10h30"),(datetime.time(11,15,0),"11h15"),(datetime.time(12,00,0),"12h"),(datetime.time(12,45,0),'12h45'),(datetime.time(13,30,0),"13h30")]))