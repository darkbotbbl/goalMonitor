from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime


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
    time_tracked = models.DurationField(null=True, blank=True)
    deadline = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)

    class Meta:
        ordering = ["title", "-created", "completed",]
        verbose_name = "Daily Goal"

    def __str__(self):
        return self.title
    

class DailyGoal(Goal):
    """
        This model will be used to create only daily goals or todos
    """
    # the parent goal of a daily goal should be a weekly goal
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    parent_goal = models.ForeignKey(
        "WeeklyGoal", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="daily_goals"
    )


class WeeklyGoal(Goal):
    """
        This model will be used to create only weekly goals
    """
    parent_goal = models.ForeignKey(
        "MonthlyGoal", 
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="weekly_goals"
    )

    # access the daily goals that are associated with a weekly goal
    def get_daily_goals(self):
        return self.daily_goals.all()


class MonthlyGoal(Goal):
    """
        This model will be used to create only monthly goals
    """
    parent_goal = models.ForeignKey(
        "QuarterlyGoal", 
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="monthly_goals"
    )

    # access the weekly goals that are associated with a monthly goal
    def get_weekly_goals(self):
        return self.weekly_goals.all()

class QuarterlyGoal(Goal):
    """
        This model will be used to create only quarterly goals
    """
    parent_goal = models.ForeignKey(
        "YearlyGoal", 
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="quarterly_goals",
    )

    # access the monthly goals that are associated with a quarterly goal
    def get_monthly_goals(self):
        return self.monthly_goals.all()

class YearlyGoal(Goal):
    """
        This model will be used to create only yearly goals
    """
    # access the quarterly goals that are associated with a yearly goal
    def get_quarterly_goals(self):
        return self.quarterly_goals.all()
