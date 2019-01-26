from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path('new_chat/',views.new_chat, name = 'new_chat')
]