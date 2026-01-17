from django.db import models
from django.contrib.auth.models import User

class Startup(models.Model):
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
