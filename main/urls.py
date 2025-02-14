from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_page, name='game_page'),
    path('ads.txt', views.serve_ads_txt, name='ads_txt'),
    path('game/', views.game, name='game'),
]
