from django import forms
from django.utils import timezone
from .models import Crepes, Apero, Meme, PetitDej
import datetime
import pytz

class CrepesForm(forms.ModelForm):
    class Meta:
        model = Crepes
        fields = ['quantity','garniture','delivery_time','delivery_date', 'delivery_place', 'comment']
        labels = {'quantity': 'Combien de crêpes?','delivery_time': 'Heure de livraison', 'delivery_date': 'Date de livraison','delivery_place': 'Lieu de livraison','comment': 'Un petit commentaire?',}
        widgets = {'delivery_date': forms.widgets.SelectDateWidget()}

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


class PetitDejForm(forms.ModelForm):
    class Meta:
        model = PetitDej
        exclude = ['user','order_time', 'delivery_date','jus','boisson_chaude']
        labels = {'delivery_time': 'Heure de livraison',
                  'delivery_place': 'Ta chambre?',
                  'jus': 'Un petit jus?',
                  'boisson_chaude': 'Ta boisson de réconfort matinal?',
                  'gout_muffin': 'Ton muffin tu le veux comment?',
                  'quatre_quart': 'Une tranche de quatre quart ça te tente?',
                  'compote':'Tu désires un peu de compote maison?',
                  'tartine': 'Une tartine pour accompagner tout ça?',
                  'comment': 'Un petit commentaire?',}
        widgets = {'quatre_quart' : forms.widgets.Select(choices = ((True, 'Ouiiii'),(False, 'Non'))),
                   'gout_muffin': forms.widgets.Select(choices=[('chocolat', 'chocolat'), ('nature', 'nature'), ('abricot',"confiture d'abricot"),('fraise',"confiture de fraise"),("rien","Pas de muffin pour moi merci!")]),
                   'jus': forms.widgets.Select(choices=[('orange','orange'),('pomme','pomme'),('raisin','raisin'),('rien','Pas de jus')]),
                   'boisson_chaude': forms.widgets.Select(choices = [('chocolat','Un bon chocolat chaud fait maison!'),('cafe','Un café Nespresso'),('the','Un thé vert'),('rien','Pas de boisson chaude')]),
                   'tartine': forms.widgets.Select(choices = [('abricot',"confiture d'abricot"),('fraise',"confiture de fraise"),('beurre','beurre'),('rien','Pas de tartines vous me gâtez déjà trop!')]),
                   'compote': forms.widgets.Select(choices = [('pomme','La classique pomme-vanille'),('poire',"Pomme-poire"),('rien','Pas de compote')])}

    def clean(self):
        delivery_time = self.cleaned_data['delivery_time']
        if (delivery_time < datetime.time(8,0,0)) or (delivery_time > datetime.time(12,0,0)):
            raise forms.ValidationError("Choisis une heure entre 8h et midi s'il te plaît")

class AperoForm(forms.ModelForm):
    class Meta:
        model = Apero
        fields = ['quantity','avec_alcool','delivery_time','delivery_date', 'delivery_place', 'comment']
        labels = {'quantity': 'Combien de personnes?','delivery_time': 'Heure de livraison', 'delivery_date': 'Date de livraison','delivery_place': 'Lieu de livraison','comment': 'Un petit commentaire?',}
        widgets = {'avec_alcool' : forms.widgets.Select(choices = ((True, 'avec alcool'),(False, 'sans alcool'))), 'delivery_date': forms.widgets.SelectDateWidget()}

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


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['comment']
        labels = {'comment': "Un petit mot d'amour/ Une petite blague en échange?"}


