from django.contrib import admin
from django.urls import path, include
from . views import DataView

urlpatterns = [
    path('getAPi/', DataView.as_view()),
    path('getApi/<int:id>/', DataView.as_view()),
]
