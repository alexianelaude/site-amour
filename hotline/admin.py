from django.contrib import admin
from .models import Crepes, Apero, Meme, PetitDej

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

class MemeAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'comment')

admin.site.register(Meme, MemeAdmin)

class PetitDejAdmin(admin.ModelAdmin):
    list_display = ('user', 'delivery_time','delivery_place','gout_muffin','tartine','jus','boisson_chaude','comment')
    date_hierarchy = 'delivery_date'
    ordering = ('delivery_date',)


admin.site.register(PetitDej, PetitDejAdmin)