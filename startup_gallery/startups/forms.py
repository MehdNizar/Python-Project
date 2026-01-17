from django import forms
from .models import Startup

class StartupForm(forms.ModelForm):
    class Meta:
        model = Startup
<<<<<<< HEAD
        fields = ['nom', 'description', 'email', 'telephone', 'site_web', 'ville', 'logo']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'site_web': forms.URLInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
        }
=======
        fields = ['nom', 'description', 'logo', 'email', 'telephone', 'site_web', 'ville']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de votre startup'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Décrivez votre startup', 'rows': 4}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contact@startup.ma'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+212 6XX XXX XXX'}),
            'site_web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Casablanca, Rabat...'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
