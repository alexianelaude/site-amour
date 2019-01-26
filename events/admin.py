from django.contrib import admin
from .models import Event
from django.utils.text import Truncator

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'debut', 'fin', 'apercu_description')
    prepopulated_fields = {'slug':('name',),}
    def apercu_description (self, event):
        return Truncator(event.description).chars(50, truncate = '...')


admin.site.register(Event, EventAdmin)
