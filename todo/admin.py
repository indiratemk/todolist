from django.contrib import admin
from todo.models import Task
from todo.models import Color

# Register your models here.

admin.site.register(Task)
admin.site.register(Color)
