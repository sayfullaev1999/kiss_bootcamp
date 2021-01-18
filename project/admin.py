from django.contrib import admin
from project.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    fields = ('name', 'image', 'info', 'users', 'site', 'slug')
    search_fields = ('name', 'site')
    filter_horizontal = ('users',)
    list_display = ('name', 'site')
    list_filter = ('users',)
