# Generated by Django 5.0.1 on 2024-03-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_engagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=15)),
                ('FirstName', models.CharField(max_length=100)),
                ('MiddleName', models.CharField(blank=True, max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Pincode', models.CharField(max_length=10)),
                ('Country', models.CharField(max_length=50)),
                ('DateofBirth', models.DateField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('Qualifications', models.CharField(max_length=255)),
                ('Position', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('Reportsto', models.CharField(default=None, max_length=50)),
                ('is_user', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('Profilepic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
            ],
        ),
    ]
