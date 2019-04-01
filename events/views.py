from django.shortcuts import render, get_object_or_404
import datetime
from datetime import date
from .models import Event
from django.utils import timezone
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def index(request):
    events_to_come = Event.objects.filter(debut__gte= timezone.now()).order_by('debut')
    current_events = Event.objects.filter(debut__lt = timezone.now(), fin__gte = timezone.now()).order_by('debut')
    past_events = Event.objects.filter(fin__lt= timezone.now()).order_by('debut')
    return render(request,'events/index.html',locals())

def detail(request,event_id):
    event = get_object_or_404(Event, id = event_id)
    return render(request, 'events/detail.html',locals())