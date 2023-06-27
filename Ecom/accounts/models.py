from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    email = models.EmailField(unique=True)
    mobile_no =models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=False,null=True,blank=True)
    

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS =['first_name','last_name','mobile_no','password1','password2']

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
  
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'