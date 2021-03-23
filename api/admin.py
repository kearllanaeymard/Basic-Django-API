from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['description', 'isCompleted']



admin.site.register(Task, TaskAdmin)
