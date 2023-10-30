from django.urls import path

from splendor_game import views

urlpatterns = [
    path("", views.index, name="index")
]