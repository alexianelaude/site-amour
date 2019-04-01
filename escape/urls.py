from django.urls import path

from . import views

app_name = 'escape'
urlpatterns = [
    path('',views.escape_game, name = 'escape'),

]