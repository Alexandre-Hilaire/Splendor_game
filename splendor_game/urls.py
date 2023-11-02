from django.urls import path

from splendor_game import views

urlpatterns = [
    path("", views.index, name="index"),
    path("startGame/", views.startGame, name="start"),
    path("getGame/", views.getGame, name="getGame"),
    path("takeThreeCoins/<int:player_id>", views.take_3_coins, name="take_3_coins"),
    path("actionTakeCoins/<int:player_id>", views.take_coins, name="action_take_3_coins")
]
