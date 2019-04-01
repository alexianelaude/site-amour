from .models import EscapeGame
from django import forms
import datetime
from django.utils import timezone


class EscapeGameForm(forms.Form):
    #quantity = forms.IntegerField(label = 'Combien de personnes souhaites-tu inscrire?', widget = forms.widgets.Select(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4')]))
    date = forms.DateField(widget=forms.widgets.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}), label = 'Pour quel jour?', initial = timezone.now())
    time = forms.TimeField(label = 'A quelle heure?', widget = forms.widgets.Select(choices = [(datetime.time(10,0,0), '10h'),(datetime.time(10,45,0),'10h45')]))