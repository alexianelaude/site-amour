from django import forms
from django.utils import timezone
from .models import Crepes, Apero, Meme, PetitDej, Muffin
import datetime
import pytz

class CrepesForm(forms.ModelForm):
    class Meta:
        model = Crepes
        fields = ['garniture','delivery_time','delivery_date', 'delivery_place', 'comment']
        labels = {'delivery_time': 'Heure de livraison', 'delivery_date': 'Date de livraison','delivery_place': 'Lieu de livraison','comment': 'Un petit commentaire?', 'garniture': 'Ta crêpe tu l\'aime?'}
        widgets = {'delivery_date': forms.widgets.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}),
                   'garniture': forms.widgets.Select(choices=[('chocolat', 'Au chocolat fondu'), ('nature', 'Nature'), ('abricot', "À la confiture d'abricot"),('fraise', "À la confiture de fraise")])}

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
        exclude = ['user','order_time', 'delivery_date','delivered']
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
        fields = ['quantity','delivery_time', 'delivery_place', 'vin', 'biere', 'cidre', 'cocktail', 'virgin_cocktail','vege','comment']
        labels = {'quantity': 'Combien de personnes?',
                  'delivery_time': 'Heure de livraison',
                  'delivery_place': 'Lieu de livraison',
                  'vin': 'Combien de verres de vin?',
                  'biere': 'Combien de demis de bière?',
                  'cidre': 'Combien de verres de cidre?',
                  'cocktail': 'Combien de verres du cocktail du jour ultra quali?',
                  'virgin_cocktail': 'Combien de verres du cocktail sans alcool pour démarrer la soirée en douceur?',
                  'vege': 'Combien de personnes sont végétariennes parmi vous?',
                  'comment': 'Un petit commentaire?'}

    def clean(self):
        vin = self.cleaned_data['vin']
        cidre = self.cleaned_data['cidre']
        biere = self.cleaned_data['biere']
        cocktail = self.cleaned_data['cocktail']
        virgin_cocktail = self.cleaned_data['virgin_cocktail']
        quantity = self.cleaned_data['quantity']
        if vin+cidre+biere+cocktail+virgin_cocktail > quantity:
            raise forms.ValidationError('Il y a trop de boissons, recomptez')


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['comment']
        labels = {'comment': "Un petit mot d'amour/ Une petite blague en échange?"}


class MuffinForm(forms.ModelForm):
    class Meta:
        model = Muffin
        exclude = ['user','order_time', 'delivery_date','delivered']
        labels = {'delivery_time': 'Heure de livraison: donne une heure entre 16 et 17h',
                  'delivery_place': 'Ta chambre?',
                  'gout_muffin': 'Ton muffin tu le veux comment?',
                  'comment': 'Un petit commentaire?',}
        widgets = {'gout_muffin': forms.widgets.Select(choices=[('chocolat', 'chocolat'), ('nature', 'nature'), ('abricot',"confiture d'abricot"),('fraise',"confiture de fraise")]),
                   }

    def clean_delivery_time(self):
        delivery_time = self.cleaned_data['delivery_time']
        if (delivery_time < datetime.time(16,0,0)) or (delivery_time > datetime.time(17,0,0)):
            raise forms.ValidationError("Choisis une heure entre 16h et 17h s'il te plaît")

    def clean_order_time(self):
        order_time = self.cleaned_data['order_time']
        if order_time.datetime.time > datetime.time(12,0,0):
            raise forms.ValidationError("Il est trop tard pour commander aujourd'hui, reviens demain!")
