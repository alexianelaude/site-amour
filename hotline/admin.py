from django.contrib import admin
from .models import Crepes

# Register your models here.
class CrepesAdmin(admin.ModelAdmin):
    list_display = ('delivery_date', 'delivery_time', 'delivery_place','order_time','user')
    list_filter = ('delivery_place',)
    date_hierarchy = 'delivery_date'
    ordering = ('delivery_date','delivery_time')

admin.site.register(Crepes, CrepesAdmin)