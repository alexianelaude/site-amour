from .models import Chat
from django import forms


class NewChat(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']

    def clean_message(self):
        message = self.cleaned_data['message']
        if 'piche' in message.lower():
            raise forms.ValidationError("Piche claquage")

        return message  # Ne pas oublier de renvoyer le contenu du champ traité