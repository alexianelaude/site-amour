from django import forms
from django.utils import timezone
from .models import Crepes

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





