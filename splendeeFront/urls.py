from django.urls import path, include
from . import views

app_name = "splendide"
urlpatterns = [
    path('', views.index, name="index"),
    path('getGame/', views.showGame, name="getGame")
]
