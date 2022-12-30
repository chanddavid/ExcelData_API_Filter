from django.contrib import admin
from django.urls import path, include
from . views import DataView, GetProjectFilter, GetSectorFilter, GetProjectBudget

urlpatterns = [
    path('api/post/', DataView.as_view()),
    path('api/get/project/', GetProjectFilter.as_view()),
    path('api/get/sector/', GetSectorFilter.as_view()),
    path('api/get/project/budget/', GetProjectBudget.as_view()),
]
