from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    TYPE_CHOICES = (
        ('visiteur', 'Visiteur'),
        ('gerant', 'Gérant de Startup'),
<<<<<<< HEAD
        ('investisseur', 'Investisseur'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_utilisateur = models.CharField(max_length=20, choices=TYPE_CHOICES, default='visiteur')
    ville = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
=======
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_utilisateur = models.CharField(max_length=20, choices=TYPE_CHOICES, default='visiteur')
    telephone = models.CharField(max_length=20, blank=True)
    ville = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.type_utilisateur}"
    
    class Meta:
        verbose_name = "Profil Utilisateur"
        verbose_name_plural = "Profils Utilisateurs"
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
