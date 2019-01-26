from .models import Mesure
from django import forms

class MesureForm(forms.Form):
    note = forms.ChoiceField(choices = [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')], label = 'Ma note', widget = forms.RadioSelect)
    comment = forms.CharField(label = 'Un commentaire?')

class BoiteAIdee(forms.Form):
    idee = forms.CharField(label = "Explique nous ton idée!")