from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class RegistrationForm(UserCreationForm):
   
    class Meta:
        model = Account
        fields = ['first_name','last_name','email','mobile_no','password1','password2']

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['mobile_no'].widget.attrs['placeholder'] = 'Enter Your Mobile Number'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
