from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('home.html', views.home, name='home'),    
    path('business.html', views.business, name='business'),    
    path('sports.html', views.sports, name='sports'),    
    path('entertainment.html', views.entertainment, name='entertainment'),
    path('base.html', views.base, name='base'),
    path('p1.html', views.p1, name='p1'),
]
