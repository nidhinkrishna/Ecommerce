from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountDisplay(UserAdmin):
    list_display =('email','username','first_name','last_name','mobile_no','last_login','is_active','date_joined')

   
    readonly_fields = ('password','date_joined')
    list_display_links = ('email','first_name','last_name','username')
    ordering = ('-date_joined',)
    
admin.site.register(Account,AccountDisplay)


class UserDisplay(admin.ModelAdmin):
   
    list_display = ( 'user', 'city', 'state')


admin.site.register(UserProfile,UserDisplay)
