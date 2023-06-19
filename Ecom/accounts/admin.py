from django.contrib import admin
from .models import *

# Register your models here.

class AccountDisplay(admin.ModelAdmin):
    list_display =('email','username','first_name','last_name','mobile_no','last_login','is_active','date_joined')
admin.site.register(Account,AccountDisplay)
