from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import News
from .models import Subscriber


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'date_pub')
    fields = ('title', 'image', 'body', 'is_active', 'slug')
    list_display = ('title', 'date_pub', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active',)
    actions = ('make_active', 'make_not_active')
    date_hierarchy = 'date_pub'

    def make_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, ngettext(
            '%d news was successfully marked as active.',
            '%d news were successfully marked as active.',
            updated
        ) % updated, messages.SUCCESS)

    def make_not_active(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, ngettext(
            '%d user was successfully marked as not active.',
            '%d users were successfully marked as not active.',
            updated
        ) % updated, messages.SUCCESS)

    make_active.short_description = "Mark selected news as active"
    make_not_active.short_description = "Mark selected news as not active"


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    fields = ('email', 'confirmed')
    list_display = ('email', 'confirmed')
    search_fields = ('email',)
    list_filter = ('confirmed',)
    actions = ('make_confirmed', 'make_not_confirmed')

    def make_confirmed(self, request, queryset):
        updated = queryset.update(confirmed=True)
        self.message_user(request, ngettext(
            '%d Subscriber was successfully marked as confirmed.',
            '%d Subscribers was successfully marked as confirmed.',
            updated
        ) % updated, messages.SUCCESS)

    def make_not_confirmed(self, request, queryset):
        updated = queryset.update(confirmed=False)
        self.message_user(request, ngettext(
            '%d Subscriber was successfully marked as not confirmed.',
            '%d Subscribers was successfully marked as not confirmed.',
            updated
        ) % updated, messages.SUCCESS)
