from django.db import models

# Create your models here.
class user_credentials(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username
    
    
class user_data(models.Model):
    Username= models.CharField(max_length=30)
    Password= models.CharField(max_length=15)
    FirstName= models.CharField(max_length=100)
    MiddleName= models.CharField(max_length=100, blank=True)
    LastName = models.CharField(max_length=100)
    Address= models.CharField(max_length=50)
    City= models.CharField(max_length=50)
    State= models.CharField(max_length=50)
    Pincode= models.CharField(max_length=10)
    Country= models.CharField(max_length=50)
    DateofBirth= models.DateField()
    Gender_choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    Gender= models.CharField(max_length=1, choices=Gender_choices)
    Qualifications = models.CharField(max_length=255)
    Position = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Reportsto= models.CharField(max_length=50,default= None)
    is_user = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    Profilepic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.username