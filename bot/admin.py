from django.contrib import admin
from .models import UserBot


@admin.register(UserBot)
class UserBotAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'username', 'language_bot',)
    list_filter = ('language_bot',)
    search_fields = ('chat_id', 'username')
