"""site-amour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    path('team/', include('team.urls')),
    path('partenaires/', TemplateView.as_view(template_name = 'partners.html'), name = 'partners'),
    path('tetris/', views.tetris, name='tetris'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('new_user/', views.new_user, name='new_user'),
    path('chat/',include('chat.urls')),
    path('events/',include('events.urls')),
    path('polls/',include('polls.urls')),
    path('photologue/', include('photologue.urls', namespace = 'photologue')),
    path('programme/', include('programme.urls')),
    path('hotline/', include('hotline.urls')),
    path('quiz/', TemplateView.as_view(template_name = 'quiz.html'), name='quiz'),
    path('bouffe/', TemplateView.as_view(template_name = 'bouffe.html'), name='bouffe'),
    path('escape/', include('escape.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

