from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Group


class GroupAdmin(ModelAdmin):
    list_display = ('group_name', 'group_direction', 'group_size')
    list_display_links = ('group_name', 'group_direction', 'group_size')
    fields = ('group_name', 'group_direction', 'group_size')
    readonly_fields = ('group_name',)


admin.site.register(Group, GroupAdmin)
