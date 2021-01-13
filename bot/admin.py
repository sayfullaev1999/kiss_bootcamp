from django.contrib import admin
from .models import Lesson, Teacher, Contact, Info, UserBot


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
        'lesson',
        'check_box',
        'date',
    )
    list_filter = (
        'check_box',
        'date',
    )
    fields = [
        'chat_id',
        'name',
        'phone_number',
        'lesson',
        'check_box',
    ]


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(UserBot)
class UserBotAdmin(admin.ModelAdmin):
    list_display = (
        'chat_id',
        'username',
        'language_bot',
    )
