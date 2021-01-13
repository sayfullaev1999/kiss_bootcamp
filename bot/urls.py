from django.urls import path

from bot.views import index

urlpatterns = [
    path('', index),
]