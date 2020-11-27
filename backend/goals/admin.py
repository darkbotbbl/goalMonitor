from django.contrib import admin

from .models import DailyGoal,WeeklyGoal,MonthlyGoal,QuarterlyGoal,YearlyGoal


class DailyGoalAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "completed",]


class WeeklyGoalAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "completed",]


class MonthlyGoalAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "completed",]


class QuarterlyGoalAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "completed",]


class YearlyGoalAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "completed",]


admin.site.register(DailyGoal, DailyGoalAdmin)
admin.site.register(WeeklyGoal, WeeklyGoalAdmin)
admin.site.register(MonthlyGoal, MonthlyGoalAdmin)
admin.site.register(QuarterlyGoal, QuarterlyGoalAdmin)
admin.site.register(YearlyGoal, YearlyGoalAdmin)