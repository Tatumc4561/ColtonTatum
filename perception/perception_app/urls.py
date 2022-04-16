from django.urls import path
from . import views


app_name = "perception"

urlpatterns = [
    path("", views.index, name="index"),
]

