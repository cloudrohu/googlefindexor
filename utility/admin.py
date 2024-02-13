from django.contrib import admin
import admin_thumbnails
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

from .models import *


class ApproxInline(admin.TabularInline):
    model = Approx
    extra = 1
    show_change_link = True

@admin_thumbnails.thumbnail('image')
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'title','slug','image_thumbnail']
    list_filter = ['title']
    inlines = [ApproxInline]
    list_per_page = 25


@admin_thumbnails.thumbnail('image')
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions', 'indented_title', 'image_thumbnail',
                    )
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['title']
    inlines = [ApproxInline]
    list_per_page = 25


@admin_thumbnails.thumbnail('image')
class CityAdmin(admin.ModelAdmin):
    list_display = [ 'title','slug','image_thumbnail']
    list_filter = ['state']
    inlines = [ApproxInline]
    readonly_fields = ('slug',)
    list_per_page = 25

@admin_thumbnails.thumbnail('image')
class LocalityAdmin(admin.ModelAdmin):
    list_display = [ 'title','slug','image_thumbnail']
    list_filter = ['city']
    inlines = [ApproxInline]
    search_fields = [ 'title',]
    readonly_fields = ('slug',)
    list_per_page = 25



class ApproxAdmin(admin.ModelAdmin):
    list_display = [ 'category', 'city','locality','total']
    list_filter = ['category', 'city','locality',]
    list_per_page = 25

    

class StateAdmin(admin.ModelAdmin):
    list_display = [ 'country', 'state']
    list_filter = ['country',]
    list_per_page = 25

class StateAdmin(admin.ModelAdmin):
    list_display = [ 'country', 'state']
    list_filter = ['country',]
    list_per_page = 25



admin.site.register(Category,CategoryAdmin2)
admin.site.register(City,CityAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Find_From,)
admin.site.register(Call_Status,)
admin.site.register(Approx,)
admin.site.register(SocialSite,)
admin.site.register(Country,)
admin.site.register(State,StateAdmin)
