from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    type_utilisateur = forms.ChoiceField(
        choices=UserProfile.TYPE_CHOICES,
        widget=forms.RadioSelect,
        label="Je suis un"
    )
<<<<<<< HEAD

    class Meta:
        model = User
        fields = ['username', 'email']

=======
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserProfile.objects.create(
                user=user,
                type_utilisateur=self.cleaned_data['type_utilisateur']
            )
        return user
<<<<<<< HEAD
=======
    
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
