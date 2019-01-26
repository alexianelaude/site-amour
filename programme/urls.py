from django.urls import path

from . import views

app_name = 'programme'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('avis/<int:pk>/', views.vote, name='vote'),
    path('boite-a-idee/', views.boite_a_idee, name = 'boite_a_idee')
]
