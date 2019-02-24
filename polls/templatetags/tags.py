from django import template
from django.shortcuts import get_object_or_404
from polls.models import Vote

register = template.Library()

@register.filter
def has_voted(poll, user):
    vote = get_object_or_404(Vote, user = user, question = poll)
    return vote.has_voted