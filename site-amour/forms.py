from django import forms
from django.contrib.auth.models import User

class ConnexionForm(forms.Form):
    username = forms.CharField(label = "Nom d'utilisateur", max_length = 30)
    password = forms.CharField(label = "Mot de passe", widget = forms.PasswordInput(), max_length = 30)

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {'password': forms.PasswordInput()}