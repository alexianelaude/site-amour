from django import forms

class MesureForm(forms.Form):
    comment = forms.CharField(label = 'Ton commentaire:')

class BoiteAIdee(forms.Form):
    description = forms.CharField(widget = forms.Textarea, label = "Ton idée ici:")