from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game, name='list_of_games'),
    path('game/new_game/', views.new_game, name='new_game'),
    path('game/<int:game_id>/', views.game, name='game_detail')
]
