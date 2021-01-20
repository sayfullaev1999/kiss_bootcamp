from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import Bot


urlpatterns = [
    path('', csrf_exempt(Bot.as_view()), name='bot_url'),
]