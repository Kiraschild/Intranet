# Generated by Django 4.2.7 on 2024-05-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_engagement', '0009_alter_timesheetdata_check_in_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='Salary',
            field=models.IntegerField(default=0),
        ),
    ]
