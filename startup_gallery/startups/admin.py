from django.contrib import admin
from .models import Startup

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'gerant', 'date_ajout')
    list_filter = ('ville', 'date_ajout')
    search_fields = ('nom', 'description', 'ville')
    
