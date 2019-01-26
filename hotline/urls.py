from django.urls import path

from . import views

app_name = 'hotline'
urlpatterns = [
    path('',views.new_order, name = 'home')
]