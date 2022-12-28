from django.contrib import admin
from django.urls import path, include
from . views import DataView

urlpatterns = [
    path('api/', DataView.as_view()),
    path('api/<int:id>/', DataView.as_view()),
]
