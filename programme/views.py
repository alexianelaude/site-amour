from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from django.http import HttpResponseRedirect
from .models import Mesure, Avis, Idee

from django.views import generic
from django.shortcuts import get_object_or_404

from .forms import MesureForm, BoiteAIdee

from django.views import generic
from django.contrib import messages
from django.db.models import Avg


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'programme/index.html'
    context_object_name = 'mesure_list'
    def get_queryset(self):
        return Mesure.objects.all()

def vote(request, pk):
    mesure = get_object_or_404(Mesure, pk=pk)
    form = MesureForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            comment = form.cleaned_data['comment']
            note = form.cleaned_data['note']
            avis = get_object_or_404(Avis, mesure = mesure, user = request.user)
            avis.comment = comment
            avis.note = note
            avis.save()
            messages.add_message(request, messages.SUCCESS, 'Votre commentaire a été enregistré, voici ceux des autres mineurs')
            return redirect(reverse('programme:detail', args = [mesure.id]))
    return render(request, 'programme/vote.html', locals())


def detail(request, pk):
    mesure = get_object_or_404(Mesure, pk = pk)
    reponses = Avis.objects.filter(mesure = mesure)
    return render(request, 'programme/detail.html',locals())

def boite_a_idee(request):
    form = BoiteAIdee(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            description = form.cleaned_data['description']
            idee = Idee(user = request.user, description = description)
            idee.save()
            messages.add_message(request, messages.SUCCESS, 'Votre idée a bien été envoyée!')
            return redirect(reverse('programme:index'))
    return render(request,'programme/boite_a_idee.html',locals())

