from django.contrib import admin
from Tasks.models import Task, Subtask, TaskOccurrence, SubtaskOccurrence


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'responsible', 'next_occurrence', 'active']
    list_editable = ['active']

class SubtaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'task', 'subtask_group', 'average_duration', 'active']
    list_editable = ['active']

class TaskOccurrenceAdmin(admin.ModelAdmin):
    list_display = ['task', 'duration', 'completed']
    list_editable = ['completed']

class SubtaskOccurrenceAdmin(admin.ModelAdmin):
    list_display = ['task_occurrence', 'duration', 'completed']
    list_editable = ['completed']

admin.site.register(Task, TaskAdmin)
admin.site.register(Subtask, SubtaskAdmin)
admin.site.register(TaskOccurrence, TaskOccurrenceAdmin)
admin.site.register(SubtaskOccurrence, SubtaskOccurrenceAdmin)
