from django.contrib import admin
from django.contrib.admin import ModelAdmin

from account.models import User, Sponsor, Mentor
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext
from django.contrib import messages


@admin.register(User)
class UserAdmin(UserAdmin):
    readonly_fields = ['date_joined', 'last_login']
    fieldsets = (
        (_('Personal info'), {'fields': ('image', 'username', 'first_name', 'last_name', 'password', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'last_login', 'is_active')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'image', 'email', 'password1', 'password2'),
        }),
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'last_login',)
    actions = ('make_active', 'make_not_active')
    date_hierarchy = 'date_joined'

    def make_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, ngettext(
            '%d user was successfully marked as active.',
            '%d users were successfully marked as active.',
            updated
        ) % updated, messages.SUCCESS)

    def make_not_active(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, ngettext(
            '%d user was successfully marked as not active.',
            '%d users were successfully marked as not active.',
            updated
        ) % updated, messages.SUCCESS)

    make_active.short_description = "Mark selected users as active"
    make_not_active.short_description = "Mark selected users as not active"


@admin.register(Mentor)
class MentorAdmin(ModelAdmin):
    readonly_fields = ('slug',)
    fields = ('user', 'image', 'info', 'position', 'slug')
    list_display = ('user', 'position')
    search_fields = ('user',)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    search_fields = ('name', 'site')
    list_display = ('name', 'site')
