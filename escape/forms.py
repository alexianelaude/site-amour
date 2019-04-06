from .models import EscapeGame
from django import forms
import datetime
from django.utils import timezone


class EscapeGameForm(forms.Form):
    #quantity = forms.IntegerField(label = 'Combien de personnes souhaites-tu inscrire?', widget = forms.widgets.Select(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4')]))
    time = forms.TimeField(label = 'A quelle heure souhaites-tu inscrire ton équipe?', widget = forms.widgets.Select(choices = [(datetime.time(14,0,0),"14h"),(datetime.time(14,45,0),'14h45'),(datetime.time(15,30,0),"15h30"),(datetime.time(16,15,0),"16h15"),(datetime.time(17,00,0),"17h")]))