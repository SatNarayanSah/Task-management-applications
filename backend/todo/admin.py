from django.contrib import admin

# Register your models here.
from .models import *

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(Todo, TodoAdmin)