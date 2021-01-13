from django.contrib import admin
from account.models import User, Sponsor
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('image', 'username', 'first_name', 'last_name', 'password', 'email', 'is_mentor')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    add_fieldsets = (
        (None, {
            'classes': ('wide', 'is_mentor'),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
    )
    list_filter = ('is_mentor', 'is_staff', 'is_superuser', 'is_active',)


admin.site.register(Sponsor)
