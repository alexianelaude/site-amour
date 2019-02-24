from django.shortcuts import get_list_or_404

from .models import Question, Vote
from django.contrib.auth.models import User
from datetime import date

def poll_today(request):
    poll_today = Question.objects.filter(pub_date = date.today())
    return {'poll_today': poll_today}