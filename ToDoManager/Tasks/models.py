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
        on_delete=models.CASCADE,
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
        User(),
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
