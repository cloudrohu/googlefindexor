from django.contrib import admin

# Register your models here.
import admin_thumbnails

from .models import *

class ImagesInInline(admin.TabularInline):
    model = Images
    extra = 1
    show_change_link = True

@admin_thumbnails.thumbnail('image')
class Society_BuildingAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'image_thumbnail','name', 'city','locality','developer','building_type','google_map']
    list_filter = ['id','city','locality','developer','building_type']
    inlines = [ImagesInInline,]

    list_per_page = 25

@admin_thumbnails.thumbnail('image')
class BuilderDeveloperAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'city','image_thumbnail']
    list_filter = ['city',]

    list_per_page = 25



admin.site.register(Society_Building,Society_BuildingAdmin)
admin.site.register(BuilderDeveloper,BuilderDeveloperAdmin)
admin.site.register(Images)
