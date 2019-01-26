from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('<int:event_id>/', views.detail, name = 'detail'),
    path('', views.index, name = 'index')
]