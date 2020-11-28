# Generated by Django 3.1.3 on 2020-11-27 20:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0009_auto_20201127_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlygoal',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 27, 20, 10, 26, 13404, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='quarterlygoal',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 20, 10, 26, 14393, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='weeklygoal',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 4, 20, 10, 26, 12350, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='yearlygoal',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 20, 10, 26, 15476, tzinfo=utc), null=True),
        ),
    ]
