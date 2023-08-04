from django.urls import path
from . import views

app_name = "first_example"

urlpatterns = [
    path("<name>/<int:age>/", views.greetings, name="greetings"),
]
