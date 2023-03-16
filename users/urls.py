from django.urls import path
from . import views

urlpatterns = [
    path("me", views.ME.as_view()),
]
