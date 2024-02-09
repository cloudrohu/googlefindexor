from django.contrib import admin

# Register your models here.
from .models import *

class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status','note','message','email','ip',]
    list_editable = ['status','note']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']


admin.site.register(Setting,SettingtAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
