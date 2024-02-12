from django.contrib import admin

# Register your models here.

from .models import *

class ImagesInInline(admin.TabularInline):
    model = Images
    extra = 1
    show_change_link = True


class Society_BuildingAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'city','locality']
    list_filter = ['city','locality',]
    inlines = [ImagesInInline,]

    list_per_page = 25



admin.site.register(Society_Building,Society_BuildingAdmin)
admin.site.register(Images)
