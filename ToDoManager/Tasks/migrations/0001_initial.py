# Generated by Django 4.0.1 on 2022-01-30 16:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('details', models.TextField(verbose_name='Details')),
                ('next_occurrence', models.DateTimeField(verbose_name='Next Occurrence')),
                ('due', models.DurationField(verbose_name='Due')),
                ('urgency', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Urgency')),
                ('planned_duration', models.DurationField(blank=True, null=True, verbose_name='Planned duration')),
                ('recurrence', models.DurationField(blank=True, null=True, verbose_name='Next Occurrence')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_created_by', to=settings.AUTH_USER_MODEL)),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_responsible', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskOccurrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('started_at', models.DateTimeField(blank=True, null=True, verbose_name='Started at')),
                ('completed_at', models.DateTimeField(blank=True, null=True, verbose_name='Completed at')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='Duration')),
                ('completed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_occurrence_completed_by', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='SubtaskOccurrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('started_at', models.DateTimeField(blank=True, null=True, verbose_name='Started at')),
                ('completed_at', models.DateTimeField(blank=True, null=True, verbose_name='Completed at')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='Duration')),
                ('completed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtask_occurrence_completed_by', to=settings.AUTH_USER_MODEL)),
                ('task_occurrence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.taskoccurrence')),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('details', models.TextField(verbose_name='Details')),
                ('subtask_group', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Subtask Group')),
                ('index_in_group', models.PositiveSmallIntegerField(verbose_name='Index in Group')),
                ('timing_weight', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Timing Weight')),
                ('average_duration', models.DurationField(blank=True, null=True, verbose_name='Average duration')),
                ('urgency', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Urgency')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtask_created_by', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.task')),
            ],
        ),
    ]
