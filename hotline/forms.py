from django import forms
from django.utils import timezone
from .models import Hotline

class HotlineForm(forms.ModelForm):
    class Meta:
        model = Hotline
        fields = ['order','delivery_time','delivery_date', 'delivery_place', 'comment']
        labels = {'delivery_time': 'Heure de livraison', 'delivery_date': 'Date de livraison','delivery_place': 'Lieu de livraison','comment': 'Un petit commentaire?',}




