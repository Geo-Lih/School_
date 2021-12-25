from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Student


class StudentAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'phone')
    list_display_links = ('first_name', 'last_name', 'age', 'phone')
    fields = ('first_name', 'last_name', 'age', 'phone')


admin.site.register(Student, StudentAdmin)
