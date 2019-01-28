from django.shortcuts import render
from django.views import generic
from .models import Listeux

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'team/index.html'
    context_object_name = 'listeux_list'
    def get_queryset(self):
        return Listeux.objects.all()