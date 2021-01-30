from django.core.management.base import BaseCommand
from bot.bot import bot


class Command(BaseCommand):
    help = 'Telegram Bot'

    def handle(self, *args, **kwargs):
        bot.polling(none_stop=True)
