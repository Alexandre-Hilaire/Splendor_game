from django.urls import path

from splendor_game import views


urlpatterns = [
    path("", views.index, name="index"),
    path("getGame/", views.getGame, name="getGame"),
    path("takeThreeCoins/", views.take_3_coins, name="take_3_coins"),
    path("actionTakeCoins/", views.take_coins, name="take3coins")
]
