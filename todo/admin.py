from django.contrib import admin
from todo.models import Task
from todo.models import Color
from todo.models import User

# Register your models here.

admin.site.register(Task)
admin.site.register(Color)
admin.site.register(User)
