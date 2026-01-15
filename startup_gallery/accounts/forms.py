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

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserProfile.objects.create(
                user=user,
                type_utilisateur=self.cleaned_data['type_utilisateur']
            )
        return user