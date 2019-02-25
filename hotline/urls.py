from django.urls import path
from django.contrib.auth.views import TemplateView

from . import views

app_name = 'hotline'
urlpatterns = [
    path('crepes/',views.new_crepes, name = 'crepes'),
    path('apero/', views.new_apero, name = 'apero'),
    path('', TemplateView.as_view(template_name = 'hotline/home.html'), name ='home')
]