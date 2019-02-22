from django.contrib import admin
from .models import Mesure, Avis, Idee

# Register your models here.
admin.site.register(Mesure)

class AvisAdmin(admin.ModelAdmin):
    list_display = ['note','comment','user']
    list_filter = ('note',)

admin.site.register(Avis, AvisAdmin)

admin.site.register(Idee)