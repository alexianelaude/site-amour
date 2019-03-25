from django.shortcuts import render, redirect, reverse, get_list_or_404
from .models import Crepes, Apero, Meme, PetitDej
from .forms import CrepesForm, AperoForm, MemeForm, PetitDejForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta, time
from django.core.mail import send_mail, EmailMessage
import os
import random

# Create your views here.
def new_crepes(request):
    form = CrepesForm(request.POST or None, initial = {'delivery_date':timezone.now(), 'delivery_time': timezone.now() + timedelta(hours = 1)})
    if form.is_valid():
        all_orders = Crepes.objects.filter(user = request.user)
        if len(all_orders) > 10:
            messages.add_message(request, messages.ERROR, "Tu as déjà trop commandé!")
            return render(request,'home.html')
        if request.user.is_authenticated:
            hot = form.save(commit = False)
            hot.user = request.user
            hot.save()
            messages.add_message(request, messages.SUCCESS, 'Nous avons bien recu votre commande, amusez vous sur le site en attendant qu\'elle arrive')
            return redirect(reverse('home'))
    return render(request, 'hotline/crepes.html', locals())

def new_apero(request):
    form = AperoForm(request.POST or None, initial = {'delivery_date':timezone.now(), 'delivery_time': timezone.now() + timedelta(hours = 1)})
    if form.is_valid():
        all_orders = Apero.objects.filter(user = request.user)
        if len(all_orders) > 1:
            messages.add_message(request, messages.ERROR, "Tu as déjà trop commandé!")
            return render(request,'home.html')
        if request.user.is_authenticated:
            hot = form.save(commit = False)
            hot.user = request.user
            hot.save()
            messages.add_message(request, messages.SUCCESS, 'Nous avons bien recu votre commande, amusez vous sur le site en attendant qu\'elle arrive')
            return redirect(reverse('home'))
    return render(request, 'hotline/apero.html', locals())

def random_meme():
    memes = os.listdir('media/memes/')
    k = random.randint(0, len(memes)-1)
    return memes[k]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def new_meme(request):
    form = MemeForm(request.POST or None)
    if form.is_valid():
        all_orders = Meme.objects.filter(user = request.user, order_date = timezone.now())
        if len(all_orders) > 0:
            messages.add_message(request, messages.ERROR, "Un seul meme par jour!")
            return render(request,'home.html')
        if request.user.is_authenticated:
            meme = form.save(commit = False)
            meme.user = request.user
            meme.save()
            mail = EmailMessage(
                'Voici un Meme de qualité supérieur',
                'Hey',
                'alexsingap@gmail.com',
                [meme.user.email]
            )
            mail.attach_file(BASE_DIR+'/media/memes/'+random_meme())
            mail.send()
            messages.add_message(request, messages.SUCCESS, 'Tu as bien recu un meme, check ta boîte mail!')
            return redirect(reverse('home'))
    return render(request, 'hotline/meme.html', locals())

def new_petitdej(request):
    form = PetitDejForm(request.POST or None, initial = {'delivery_time': time(8,0,0)})
    if form.is_valid():
        all_orders = PetitDej.objects.filter(user = request.user)
        if len(all_orders) > 0:
            messages.add_message(request, messages.ERROR, "Un seul petit dej par personne, désolé")
            return render(request,'home.html')
        if request.user.is_authenticated:
            hot = form.save(commit = False)
            hot.user = request.user
            hot.save()
            messages.add_message(request, messages.SUCCESS, 'Nous avons bien recu votre commande, amusez vous sur le site en attendant votre petit dej')
            return redirect(reverse('home'))
    return render(request, 'hotline/petitdej.html', locals())