from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'completed')
    list_filter = list_display


admin.site.register(Task, TaskAdmin)
