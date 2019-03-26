from django.contrib import admin
from .models import Crepes, Apero, Meme, PetitDej, Muffin

# Register your models here.

def make_delivered(modeladmin, request, queryset):
    queryset.update(delivered = True)
make_delivered.short_description = "Ces commandes ont été livrées"

class CrepesAdmin(admin.ModelAdmin):
    list_display = ('delivery_date', 'delivery_time', 'delivery_place','order_time','user', 'delivered')
    list_filter = ('delivery_place','delivered')
    date_hierarchy = 'delivery_date'
    ordering = ('delivery_date','delivery_time')
    actions = [make_delivered]

admin.site.register(Crepes, CrepesAdmin)

class AperoAdmin(admin.ModelAdmin):
    list_display = ('delivery_time', 'delivery_place','order_time','user','vin','biere','cidre','cocktail','virgin_cocktail','vege', 'delivered')
    list_filter = ('delivery_place','delivered')
    ordering = ('delivery_time',)
    actions = [make_delivered]

admin.site.register(Apero, AperoAdmin)

class MemeAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'comment')

admin.site.register(Meme, MemeAdmin)

class PetitDejAdmin(admin.ModelAdmin):
    list_display = ('user', 'delivery_time','delivery_place','gout_muffin','tartine','jus','boisson_chaude','comment','delivered')
    ordering = ('delivery_time','delivered')
    actions = [make_delivered]


admin.site.register(PetitDej, PetitDejAdmin)

class MuffinAdmin(admin.ModelAdmin):
    list_display = ('user', 'delivery_time','delivery_place','gout_muffin','comment', 'delivered')
    ordering = ('delivery_time','delivered')
    actions = [make_delivered]


admin.site.register(Muffin, MuffinAdmin)