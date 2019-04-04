from .models import EscapeGame
from django import forms
import datetime
from django.utils import timezone


class EscapeGameForm(forms.Form):
    #quantity = forms.IntegerField(label = 'Combien de personnes souhaites-tu inscrire?', widget = forms.widgets.Select(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4')]))
    time = forms.TimeField(label = 'A quelle heure souhaites-tu inscrire ton équipe?', widget = forms.widgets.Select(choices = [(datetime.time(17,0,0),"17h"),(datetime.time(17,45,0),'17h45'),(datetime.time(18,30,0),"18h30"),(datetime.time(19,15,0),"19h15"),(datetime.time(20,00,0),"20h"),(datetime.time(20,45,0),"20h45")]))