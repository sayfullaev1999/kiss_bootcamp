from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin
from django.utils.translation import ngettext

from course.models import Course, ContactUs


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    readonly_fields = ('slug',)
    fields = ('name', 'image', 'info', 'mentor', 'slug')
    list_display = ('name',)
    filter_horizontal = ('mentor',)
    list_filter = ('mentor',)
    search_fields = ('name',)


@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    readonly_fields = ('chat_id',)
    fields = ('chat_id', 'full_name', 'phone_number', 'course', 'check_box')
    list_display = ('full_name', 'course', 'date', 'check_box')
    list_filter = ('check_box', 'date')
    actions = ('make_viewed', 'make_not_viewed')
    search_fields = ('full_name', 'phone_number', 'course')

    def make_viewed(self, request, queryset):
        updated = queryset.update(check_box=True)
        self.message_user(request, ngettext(
            '%d contact us was successfully marked as viewed.',
            '%d contact was successfully marked as viewed',
            updated
        ) % updated, messages.SUCCESS)

    def make_not_viewed(self, request, queryset):
        updated = queryset.update(check_box=False)
        self.message_user(request, ngettext(
            '%d contact was successfully marked as not viewed',
            '%d contact was successfully marked as not viewed',
            updated
        ) % updated, messages.SUCCESS)

    make_viewed.short_description = "Mark selected contact us as viewed"
    make_not_viewed.short_description = "Mark selected contact us as not viewed"
