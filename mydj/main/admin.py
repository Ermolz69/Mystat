from django.contrib import admin
from .models import Task, Lesson, Feedback

# Register your models here.
admin.site.register(Task)
admin.site.register(Lesson)
admin.site.register(Feedback)
