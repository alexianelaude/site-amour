from django import forms
from django.utils import timezone
from .models import Crepes
import datetime
import pytz

class CrepesForm(forms.ModelForm):
    class Meta:
        model = Crepes
        fields = ['quantity','garniture','delivery_time','delivery_date', 'delivery_place', 'comment']
        labels = {'quantity': 'Combien de crêpes?','delivery_time': 'Heure de livraison', 'delivery_date': 'Date de livraison','delivery_place': 'Lieu de livraison','comment': 'Un petit commentaire?',}

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity > 20:
            raise forms.ValidationError("Laisse en aux autres stp!")

        return quantity

    def clean(self):
        delivery_date = self.cleaned_data['delivery_date']
        delivery_time = self.cleaned_data['delivery_time']
        delivery = datetime.datetime.combine(delivery_date, delivery_time)
        delivery = pytz.timezone('Europe/Amsterdam').localize(delivery)
        if delivery < timezone.now():
            raise forms.ValidationError('Laisse nous un peu de temps!')





