from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from django.http import HttpResponseRedirect
from .models import Question, Choice, Vote

from django.views import generic
from django.shortcuts import get_object_or_404

from django.utils import timezone

# Create your views here.
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if request.user.is_authenticated:
            vote = get_object_or_404(Vote, question = question, user = request.user)
            vote.has_voted = True
            vote.save()
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def detail(request, pk):
    question = get_object_or_404(Question, pk = pk)
    if request.user.is_authenticated:
        vote = get_object_or_404(Vote, question = question, user = request.user).has_voted
    else:
        vote = True
    return render(request, 'polls/detail.html',locals())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'