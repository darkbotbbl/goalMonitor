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
    )
    description = models.TextField(
        help_text="Write a bit of description about this goal",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    duration = models.DurationField()
    completed = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)

    class Meta:
        ordering = ["title", "-created", "completed",]

class DailyGoal(Goal):
    """
        This model will be used to create only daily goals or todos
    """
