from django.contrib import admin

# Register your models here.

from .models import *

class ImagesInInline(admin.TabularInline):
    model = Images
    extra = 1
    show_change_link = True


class Society_BuildingAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'city','locality','building_type','google_map']
    list_filter = ['city','locality','building_type']
    inlines = [ImagesInInline,]

    list_per_page = 25



admin.site.register(Society_Building,Society_BuildingAdmin)
admin.site.register(Images)
