from django.contrib import admin

from .models import Profile,Sprint,TaskStatus,Task

admin.site.register(Profile)
admin.site.register(Sprint)
admin.site.register(TaskStatus)
admin.site.register(Task)