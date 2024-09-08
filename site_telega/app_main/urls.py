from django.contrib import admin
from django.urls import path, include

from app_main import views



patterns = [
    path("", views.success),
    ]

urlpatterns = [
    path("form/", include(patterns)),
]
