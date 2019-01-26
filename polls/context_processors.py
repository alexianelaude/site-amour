from .models import Question
from datetime import date

def poll_today(request):
    poll_today = Question.objects.filter(pub_date = date.today())
    return {'poll_today': poll_today}