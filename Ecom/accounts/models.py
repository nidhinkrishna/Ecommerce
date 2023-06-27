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


