# Generated by Django 3.1.3 on 2020-11-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0011_auto_20201127_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailygoal',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='monthlygoal',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='quarterlygoal',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='weeklygoal',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='yearlygoal',
            name='deadline',
        ),
        migrations.AddField(
            model_name='goal',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
