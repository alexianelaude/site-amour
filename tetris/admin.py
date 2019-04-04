from django.contrib import admin
from .models import TetrisModel

# Register your models here.
class TetrisAdmin(admin.ModelAdmin):
    list_display = ('score', 'user')
    list_filter = ('score','user')

admin.site.register(TetrisModel, TetrisAdmin)
