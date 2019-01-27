from django import forms
from django.contrib.auth.models import User

class ConnexionForm(forms.Form):
    username = forms.CharField(label = "Nom d'utilisateur", max_length = 30)
    password = forms.CharField(label = "Mot de passe", widget = forms.PasswordInput(), max_length = 30)

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']
        widgets = {'password': forms.PasswordInput()}
    def clean_email(self):
        email = self.cleaned_data['email']
        if 'mines-paristech.fr' not in email:
            raise forms.ValidationError("Il faut mettre son adresse des Mines!")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email a déjà été pris")
        return email