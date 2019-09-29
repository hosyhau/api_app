from django.contrib import admin
from todoapp.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ("todo_id", "name", "done", "date_created")
    list_filter = ("done", "date_created")

admin.site.register(Todo, TodoAdmin)