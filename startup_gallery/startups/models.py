from django.db import models
from django.contrib.auth.models import User

class Startup(models.Model):
<<<<<<< HEAD
    nom = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    site_web = models.URLField(blank=True)
    ville = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    gerant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
=======
    nom = models.CharField(max_length=200, verbose_name="Nom de la startup")
    description = models.TextField(verbose_name="Description")
    logo = models.ImageField(upload_to='startups/', verbose_name="Logo")
    email = models.EmailField(verbose_name="Email de contact")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    site_web = models.URLField(blank=True, verbose_name="Site web")
    ville = models.CharField(max_length=100, verbose_name="Ville")
    gerant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Gérant")
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Startup"
        verbose_name_plural = "Startups"
        ordering = ['-date_ajout']
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
