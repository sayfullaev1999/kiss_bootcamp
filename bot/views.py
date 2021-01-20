from telebot import types
from django.http import HttpRequest
from bot.bot import bot

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request: HttpRequest):
    # Сюда должны получать сообщения от телеграм и далее обрабатываться ботом
    json_str = request.body.decode('UTF-8')
    update = types.Update.de_json(json_str)
    bot.process_new_updates([update])

    return HttpResponse()
