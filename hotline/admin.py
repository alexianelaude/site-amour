from django.contrib import admin
from .models import Crepes, Apero

# Register your models here.
class CrepesAdmin(admin.ModelAdmin):
    list_display = ('delivery_date', 'delivery_time', 'delivery_place','order_time','user')
    list_filter = ('delivery_place',)
    date_hierarchy = 'delivery_date'
    ordering = ('delivery_date','delivery_time')

admin.site.register(Crepes, CrepesAdmin)

class AperoAdmin(admin.ModelAdmin):
    list_display = ('delivery_date', 'delivery_time', 'delivery_place','order_time','user','avec_alcool')
    list_filter = ('delivery_place',)
    date_hierarchy = 'delivery_date'
    ordering = ('delivery_date','delivery_time')

admin.site.register(Apero, AperoAdmin)