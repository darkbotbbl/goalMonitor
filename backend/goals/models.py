from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()


# Base Goal Class
class Goal(models.Model):
    """
        Base class for a goal, has common attributes and methods needed for goal
        creation and tracking
    """
    title = models.CharField(
        max_length=255,
        help_text="name of the goal, keep it simple",
        default="",
        blank=False,
        null=False,
    )
    description = models.TextField(
        help_text="Write a bit of description about this goal",
        default="",
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True)
    duration = models.DurationField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)

    class Meta:
        ordering = ["title", "-created", "completed",]
        verbose_name = "Daily Goal"


class DailyGoal(Goal):
    """
        This model will be used to create only daily goals or todos
    """
    # the parent goal of a daily goal should be a weekly goal
    parent_goal = models.ForeignKey(
        "WeeklyGoal", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


class WeeklyGoal(Goal):
    """
        This model will be used to create only weekly goals
    """
    parent_goal = models.ForeignKey(
        "MonthlyGoal", 
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )


class MonthlyGoal(Goal):
    """
        This model will be used to create only weekly goals
    """
    parent_goal = models.ForeignKey(
        "QuartelyGoal", 
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )


class QuartelyGoal(Goal):
    """
        This model will be used to create only weekly goals
    """
    parent_goal = models.ForeignKey(
        "YearlyGoal", 
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )


class YearlyGoal(Goal):
    """
        This model will be used to create only weekly goals
    """
    pass