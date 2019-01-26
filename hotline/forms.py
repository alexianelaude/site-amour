from django import forms
from django.utils import timezone

class HotlineForm(forms.Form):
    order = forms.ChoiceField(choices = [('crepes','des crêpes'),('bisous','des bisous')], label = 'Je désire:', widget = forms.RadioSelect)
    delivery_time = forms.DateTimeField(label = 'Heure de livraison', widget = forms.widgets.DateTimeInput)
    delivery_place = forms.CharField(label = 'Lieu de livraison')
    comment = forms.CharField()

    def clean_order(self):
        delivery_time = self.cleaned_data['delivery_time']
        if delivery_time <= timezone.now():
            raise forms.ValidationError("Laisse nous un peu de temps pour te livrer!")

        return delivery_time  # Ne pas oublier de renvoyer le contenu du champ traité
