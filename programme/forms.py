from django import forms

class MesureForm(forms.Form):
    note = forms.IntegerField(widget = forms.widgets.Select(choices = [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]))
    comment = forms.CharField(widget = forms.Textarea, label = 'Ton commentaire:')

class BoiteAIdee(forms.Form):
    description = forms.CharField(widget = forms.Textarea, label = "Ton idée ici:")