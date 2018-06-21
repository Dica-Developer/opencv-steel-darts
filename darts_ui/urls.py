from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_game/', views.new_game, name='new_game'),
]
