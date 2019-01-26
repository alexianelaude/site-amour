from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Vote


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text','pub_date']
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

class VoteAdmin(admin.ModelAdmin):
    list_display = ['user','has_voted','question']
    search_fields = ['user','question']

admin.site.register(Vote, VoteAdmin)