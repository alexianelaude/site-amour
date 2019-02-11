from django.shortcuts import render, redirect, reverse
from .models import Hotline
from .forms import CrepesForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

# Create your views here.
def new_crepes(request):
    form = CrepesForm(request.POST or None, initial = {'delivery_date':timezone.now(), 'delivery_time': timezone.now() + timedelta(hours = 1)})
    if form.is_valid():
        if request.user.is_authenticated:
            hot = form.save(commit = False)
            hot.user = request.user
            hot.save()
            messages.add_message(request, messages.SUCCESS, 'Nous avons bien recu votre commande, amusez vous sur le site en attendant qu\'elle arrive')
            return redirect(reverse('home'))
    return render(request, 'hotline/crepes.html', locals())


