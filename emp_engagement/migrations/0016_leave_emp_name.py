# Generated by Django 4.2.7 on 2024-05-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_engagement', '0015_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='emp_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
