from django.urls import path
from .views import *


urlpatterns = [
path('Game',GametList.as_view(),name='game_list'),
path('Game/<int:pk>',game_detail.as_view(),name='game_detail'),
]
