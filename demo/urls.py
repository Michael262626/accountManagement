from django.urls import path

from account import admin
from demo import views


urlpatterns = [
    path("hello", views.say_hello),
    path("hello/<str:name>/", views.say_hello),
]
