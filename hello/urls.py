from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>/", views.greet, name="greet"),
    path("nam/", views.nam, name="nam"),
    path("jon/", views.jon, name="jon")
]
