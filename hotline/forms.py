from django import forms
from django.utils import timezone
from .models import Crepes, Apero, Meme, PetitDej, Muffin
import datetime
import pytz

class CrepesForm(forms.ModelForm):
    class Meta:
        model = Crepes
        fields = ['garniture','delivery_time', 'delivery_place', 'comment']
        labels = {'delivery_time': "Heure de livraison, pour l'indiquer, merci de garder le format d'heure 'hh:mm' (par exemple 08:00) pour ne pas avoir d'erreur",
                  'delivery_place': 'Lieu de livraison','comment': 'Un petit commentaire?', 'garniture': 'Ta crêpe tu l\'aimes?'}
        widgets = {'garniture': forms.widgets.Select(choices=[ ('nature', 'Nature'), ('abricot', "À la confiture d'abricot"),('fraise', "À la confiture de fraise"),('chocolat','Au chocolat fondu'),('sucre','Au sucre'),('sucre-citron', 'Sucre-citron'),('miel','Au miel'),('erable',"Au sirop d'érable"),('caramel',"Au caramel beurre-salé"),('banane-choc',"Banane-choco"),('pomme-choc',"Pomme-choco"),('poire-choco',"Poire-choco"),('coco',"Noix de coco rapée"),('amande-choco',"Amande effilées et chocolat"),('glace',"Glace au citron"),('creme-marron',"Crème de marron"),('flambee',"Une crêpes flambée!!! Incroyable!!")])}

    def clean(self):
        delivery_date = timezone.now()
        delivery_time = self.cleaned_data['delivery_time']
        delivery = datetime.datetime.combine(delivery_date, delivery_time)
        delivery = pytz.timezone('Europe/Amsterdam').localize(delivery)
        #if delivery + datetime.timedelta(minutes= 1) < timezone.now():
            #raise forms.ValidationError('Laisse nous un peu de temps!')
        if delivery_time < datetime.time(8,0,0) or delivery_time > datetime.time(18,30,0):
            raise forms.ValidationError('La hotline crêpes ne fonctionne que de 8h à 18h30! ')


class PetitDejForm(forms.ModelForm):
    class Meta:
        model = PetitDej
        fields = ['delivery_time', 'delivery_place']
        labels = {'delivery_time': "Heure de livraison, pour indiquer l'heure de livraison, merci de garder le format d'heure 'hh:mm' (par exemple 08:00) pour ne pas avoir d'erreur",
                  'delivery_place': 'Ta chambre?',
                  'comment': 'Un petit commentaire?',}

    def clean(self):
        delivery_time = self.cleaned_data['delivery_time']
        if (delivery_time < datetime.time(18,30,0)) or (delivery_time > datetime.time(20,0,0)):
            raise forms.ValidationError("Choisis une heure entre 18h30 et 20h s'il te plaît")

class AperoForm(forms.ModelForm):
    class Meta:
        model = Apero
        fields = ['quantity','delivery_time', 'delivery_place', 'vin', 'biere', 'cidre', 'cocktail', 'virgin_cocktail','vege','comment']
        labels = {'quantity': 'Combien de personnes?',
                  'delivery_time': "Heure de livraison: pour indiquer l'heure de livraison, merci de garder le format d'heure 'hh:mm' (par exemple 08:00) pour ne pas avoir d'erreur",
                  'delivery_place': 'Lieu de livraison',
                  'vin': 'Combien de verres de vin?',
                  'biere': 'Combien de demis de bière?',
                  'cidre': 'Combien de verres de cidre?',
                  'cocktail': 'Combien de verres de mojito (le fameux que tu as tant apprécié au before de jeudi)?',
                  'virgin_cocktail': 'Combien de verres de mojito sans alcool ?',
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
        delivery_time = self.cleaned_data['delivery_time']
        delivery = datetime.datetime.combine(timezone.now(), delivery_time)
        delivery = pytz.timezone('Europe/Amsterdam').localize(delivery)
        #if delivery + datetime.timedelta(minutes = 1) < timezone.now():
            #raise forms.ValidationError('Laisse nous un peu de temps!')
        if delivery_time < datetime.time(18,30,0):
            raise forms.ValidationError('Les apéros ne sont livrés qu\'à partir de 18h30')
        if delivery_time > datetime.time(20,45,0):
            raise forms.ValidationError('Il n\'y a plus d\'apéros après 20h45')


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['comment']
        labels = {'comment': "Un petit mot d'amour/ Une petite blague en échange?"}


class MuffinForm(forms.ModelForm):
    class Meta:
        model = Muffin
        fields = ['delivery_time', 'delivery_place', 'gout_muffin', 'comment']
        labels = {'delivery_time': "Heure de livraison: donne une heure entre 16 et 17h, pour indiquer l'heure de livraison, merci de garder le format d'heure 'hh:mm' (par exemple 08:00) pour ne pas avoir d'erreur",
                  'delivery_place': 'Ta chambre?',
                  'gout_muffin': 'Ton muffin tu le veux comment?',
                  'comment': 'Un petit commentaire?',}
        widgets = {'gout_muffin': forms.widgets.Select(choices=[('chocolat', 'chocolat'), ('nature', 'nature'), ('abricot',"confiture d'abricot"),('fraise',"confiture de fraise")]),
                   }

    def clean(self):
        delivery_time = self.cleaned_data['delivery_time']
        if (delivery_time < datetime.time(16,0,0)) or (delivery_time > datetime.time(17,0,0)):
            raise forms.ValidationError("Choisis une heure entre 16h et 17h s'il te plaît")

    def clean_order_time(self):
        order_time = self.cleaned_data['order_time']
        if order_time.datetime.time > datetime.time(12,0,0):
            raise forms.ValidationError("Il est trop tard pour commander aujourd'hui, reviens demain!")



