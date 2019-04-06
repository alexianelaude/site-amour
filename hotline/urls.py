from django.urls import path
from django.contrib.auth.views import TemplateView

from . import views

app_name = 'hotline'
urlpatterns = [
    path('crepes/',views.new_crepes, name = 'crepes'),
    path('apero/', views.new_apero, name = 'apero'),
    path('petitdej/', views.new_petitdej, name='petitdej'),
    path('meme/', views.new_meme, name = 'meme'),
    path('muffin/', views.new_muffin, name='muffin'),
    path('', TemplateView.as_view(template_name = 'hotline/home.html'), name ='home'),
    path('meme/display', TemplateView.as_view(template_name='hotline/meme_display.html'), name = 'meme_display'),
    path('tel', TemplateView.as_view(template_name = 'hotline/tel.html'), name = 'tel')
]