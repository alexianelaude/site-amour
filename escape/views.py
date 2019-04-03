from django.shortcuts import render
from .forms import EscapeGameForm
from .models import EscapeGame
import datetime
import pytz
from django.contrib import messages
from django.utils import timezone

# Create your views here.

def escape_game(request):
    form = EscapeGameForm(request.POST or None)
    if form.is_valid():
        time = form.cleaned_data['time']
        date = timezone.now()
        full_date = datetime.datetime.combine(date, time)
        full_date = pytz.timezone('Europe/Amsterdam').localize(full_date)
        all_orders = EscapeGame.objects.filter(datetime = full_date)
        a_inscrire = 4
        deja_inscrit = 0
        for order in all_orders:
            deja_inscrit += order.quantity
        if deja_inscrit + a_inscrire > 4:
            messages.add_message(request, messages.ERROR, "Désolé mais il n'y a plus assez de places disponibles à cet horaire")
            return render(request, 'escape.html', locals())
        else:
            escape = EscapeGame.objects.create(user = request.user, quantity = a_inscrire, datetime = full_date)
            escape.save()
            messages.add_message(request, messages.SUCCESS, "Vous avez bien reservé votre créneau d'escape game, ne l'oubliez pas!")
            return render(request, 'home.html')
    return render(request, 'escape.html', locals())
