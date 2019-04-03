from django.urls import path

from tetris import views

app_name = 'tetris'
urlpatterns = [
    path('', views.tetris, name='tetris'),
    path('get_scores/', views.get_scores, name ='get_scores'),
    path('add_score/', views.add_score, name ='add_score')
]