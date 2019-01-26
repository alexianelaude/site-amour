from django.contrib import admin
from .models import Mesure, Avis

# Register your models here.
admin.site.register(Mesure)

class AvisAdmin(admin.ModelAdmin):
    list_display = ['has_voted','note','comment','user']

admin.site.register(Avis, AvisAdmin)