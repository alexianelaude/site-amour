from django.contrib.auth import authenticate, login, logout
from .forms import ConnexionForm, NewUserForm
from django.shortcuts import render, redirect
from django.urls import reverse
from profil.models import Profil
from django.contrib.auth.models import User

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect(reverse('home'))
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse('home'))

def new_user(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = User.objects.create_user(username = username, password = password)
        user.save()
        mineur = Profil(user=user)
        mineur.save()
        sauvegarde = True
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'home.html',{'sauvegarde': sauvegarde})
    return render(request, 'new_user.html', {'form': form})