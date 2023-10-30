from django.urls import path

from splendor_game import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getGame/", views.getGame, name="getGame"),
    path("seeHand/<int:player_id>/", views.seeHand, name="hand")
]