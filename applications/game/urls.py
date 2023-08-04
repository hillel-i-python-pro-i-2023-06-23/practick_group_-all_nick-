from django.urls import path
from applications.game import views

app_name = "game"

urlpatterns = [
    path("", views.index, name="start_game"),
]
