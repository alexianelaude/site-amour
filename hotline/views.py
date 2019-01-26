from django.shortcuts import render
from .models import Hotline
from .forms import HotlineForm
from django.contrib import messages

# Create your views here.
def new_order(request):
    form = HotlineForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            hot = form.save(commit = False)
            hot.user = request.user
            hot.save()
            messages.add_message(request, messages.SUCCESS, 'Nous avons bien recu votre commande, amusez vous sur le site en attendant qu\'elle arrive')
            return render(request, 'home.html')
    return render(request, 'hotline/home.html', locals())


