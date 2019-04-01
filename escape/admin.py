from django.contrib import admin
from .models import EscapeGame

# Register your models here.
class EscapeGameAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'user','quantity')
    list_filter = ('datetime',)
    date_hierarchy = 'datetime'
    ordering = ('datetime',)

admin.site.register(EscapeGame, EscapeGameAdmin)