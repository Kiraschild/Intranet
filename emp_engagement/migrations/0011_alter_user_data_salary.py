# Generated by Django 4.2.7 on 2024-05-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_engagement', '0010_user_data_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='Salary',
            field=models.CharField(max_length=15),
        ),
    ]
