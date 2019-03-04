from django.contrib.auth import authenticate, login, logout
from .forms import ConnexionForm, NewUserForm
from django.shortcuts import render, redirect
from django.urls import reverse
from profil.models import Profil
from django.contrib.auth.models import User
from django.contrib import messages


def connexion(request):
    error = False

    if request.method == "POST":
        connexion_form = ConnexionForm(request.POST)
        if connexion_form.is_valid():
            username = connexion_form.cleaned_data["username"]
            password = connexion_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect(reverse('home'))
            else: # sinon une erreur sera affichée
                error = True
    else:
        connexion_form = ConnexionForm()

    return render(request, 'connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse('home'))

def new_user(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        email = form.cleaned_data["email"]
        user = User.objects.create_user(username = username, password = password, email = email)
        user.save()
        mineur = Profil(user=user)
        mineur.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Bienvenue %s, ton compte a bien été enregistré" % (user.username))
        return render(request, 'home.html')
    return render(request, 'new_user.html', {'form': form})