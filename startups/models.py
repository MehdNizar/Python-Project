from django.db import models
from django.conf import settings  # Import essentiel

class Startup(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    site_web = models.URLField(blank=True)
    ville = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    # C'est ici que la correction se fait :
    gerant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom