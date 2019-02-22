from django.shortcuts import render, redirect, reverse, get_list_or_404
from .models import Crepes
from .forms import CrepesForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta


# Create your views here.
def new_crepes(request):
    form = CrepesForm(request.POST or None, initial = {'delivery_date':timezone.now(), 'delivery_time': timezone.now() + timedelta(hours = 1)})
    if form.is_valid():
        all_orders = get_list_or_404(Crepes, user = request.user)
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


