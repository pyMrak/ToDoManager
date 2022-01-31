from django.db import models
from django.db.models.fields import TextField
from rest_framework.fields import CharField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _


class Task(models.Model):

    created_by = models.ForeignKey(
        get_user_model(),
        related_name='task_created_by',
        null=True,
        on_delete=models.SET_NULL,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    active = models.BooleanField(
        default=True,
    )

    name = models.CharField(
        _('Name'),
        max_length=255,
    )

    details = models.TextField(
        _('Details')
    )

    responsible = models.ForeignKey(
        User,
        related_name='task_responsible',
        on_delete=models.CASCADE,
    )

    next_occurrence = models.DateTimeField(
        _('Next Occurrence'),
    )

    due = models.DurationField(
        _('Due'),
    )

    urgency = models.PositiveSmallIntegerField(
        _('Urgency'),
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    planned_duration = models.DurationField(
        _('Planned duration'),
        null=True,
        blank=True,
    )

    recurrence = models.DurationField(
        _('Next Occurrence'),
        null=True,
        blank=True,
    )


class Subtask(models.Model):

    created_by = models.ForeignKey(
        get_user_model(),
        related_name='subtask_created_by',
        null=True,
        on_delete=models.SET_NULL,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    active = models.BooleanField(
        default=True,
    )

    name = models.CharField(
        _('Name'),
        max_length=255,
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )

    details = models.TextField(
        _('Details')
    )

    subtask_group = models.PositiveSmallIntegerField(
        _('Subtask Group'),
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    index_in_group = models.PositiveSmallIntegerField(
        _('Index in Group'),
    )

    timing_weight = models.PositiveSmallIntegerField(
        _('Timing Weight'),
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    average_duration = models.DurationField(
        _('Average duration'),
        null=True,
        blank=True,
    )

    urgency = models.PositiveSmallIntegerField(
        _('Urgency'),
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )


class TaskOccurrence(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )

    completed = models.BooleanField(
        _('Completed'),
        default=False,
    )

    started_at = models.DateTimeField(
        _('Started at'),
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        _('Completed at'),
        null=True,
        blank=True,
    )

    completed_by = models.ForeignKey(
        User,
        related_name='task_occurrence_completed_by',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    duration = models.DurationField(
        _('Duration'),
        null=True,
        blank=True,
    )


class SubtaskOccurrence(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    subtask = models.ForeignKey(
        TaskOccurrence,
        related_name='subtask_occurrence_subtask',
        on_delete=models.CASCADE,
    )

    task_occurrence = models.ForeignKey(
        TaskOccurrence,
        null=True,
        on_delete=models.SET_NULL,
    )

    completed = models.BooleanField(
        _('Completed'),
        default=False,
    )

    started_at = models.DateTimeField(
        _('Started at'),
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        _('Completed at'),
        null=True,
        blank=True,
    )

    completed_by = models.ForeignKey(
        User,
        related_name='subtask_occurrence_completed_by',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    duration = models.DurationField(
        _('Duration'),
        null=True,
        blank=True,
    )
