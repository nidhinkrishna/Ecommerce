from django.contrib import admin
from .models import *

# Register your models here.

class AccountDisplay(admin.ModelAdmin):
    list_display =('email','username','first_name','last_name','mobile_no','last_login','is_active','date_joined')

   
    readonly_fields = ('password','date_joined')
    list_display_links = ('email','first_name','last_name','username')
    ordering = ('-date_joined',)
    
admin.site.register(Account,AccountDisplay)
