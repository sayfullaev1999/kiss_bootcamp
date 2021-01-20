from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.generic.base import View
from telebot import types
from .bot import bot


class Bot(View):
    def get(self, request):
        raise PermissionDenied()

    def post(self, request):
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return HttpResponse('<h1>Success</h1>')