from django.contrib import admin
from .models import Task



@admin.register(Task)
class AdminDisplay(admin.ModelAdmin):
    list_display = [
        'title',
        'decription',
        'completed',
        'created',

    ]
