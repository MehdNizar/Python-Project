from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'type_utilisateur', 'ville')
    list_filter = ('type_utilisateur',)
    search_fields = ('user__username', 'ville')
<<<<<<< HEAD
    
    
=======
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
