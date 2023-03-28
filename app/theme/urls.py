from django.urls import path
from .views import ThemeView

urlpatterns = [
    path('', ThemeView.as_view(), name='theme-list'),
    path('<str:theme>', ThemeView.as_view(), name='theme-unique'),
]