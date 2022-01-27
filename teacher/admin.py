from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Teacher


class TeacherAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'phone')
    list_display_links = ('first_name', 'last_name', 'age', 'phone')
    fields = ('first_name', 'last_name', 'age', 'phone')
    readonly_fields = ('age',)


admin.site.register(Teacher, TeacherAdmin)
