from .models import Event
from datetime import date
from django.utils import timezone

def events_today(request):
    list_events = Event.objects.filter(debut__date = date.today())
    return ({'events_today': list_events})

def all_events(request):
    return({'events': Event.objects.all()})