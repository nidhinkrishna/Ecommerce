from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactDisplay(admin.ModelAdmin):
    list_display = ('name','email','subject','date_added')
    readonly_fields = ('name','email','subject','date_added')

admin.site.register(Contact,ContactDisplay)
