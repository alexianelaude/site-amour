from django.shortcuts import render, redirect
from .forms import NewChat
from django.http import HttpResponseRedirect

from .models import Chat

# Create your views here.
def new_chat(request):
    form = NewChat(request.POST or None)
    if form.is_valid():
        chat = form.save(commit = False)
        if request.user.is_authenticated:
            chat.user = request.user
            chat.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

