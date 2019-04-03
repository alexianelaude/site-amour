from .models import EscapeGame
from django import forms
import datetime
from django.utils import timezone


class EscapeGameForm(forms.Form):
    #quantity = forms.IntegerField(label = 'Combien de personnes souhaites-tu inscrire?', widget = forms.widgets.Select(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4')]))
    time = forms.TimeField(label = 'A quelle heure?', widget = forms.widgets.Select(choices = [(datetime.time(15,0,0), '15h'),(datetime.time(15,45,0),'15h45'), (datetime.time(16,30,0),'16h30'),(datetime.time(17,15,0),"17h15"),(datetime.time(18,0,0),'18h'),(datetime.time(18,45,0),"18h45"),(datetime.time(19,30,0),"19h30"),(datetime.time(20,15,0),"20h15"),(datetime.time(21,0,0),"21h")]))