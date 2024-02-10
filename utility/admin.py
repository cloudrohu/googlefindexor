from django.contrib import admin
import admin_thumbnails

# Register your models here.

from .models import *


class ApproxInline(admin.TabularInline):
    model = Approx
    extra = 1
    show_change_link = True

@admin_thumbnails.thumbnail('image')
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'title','slug']
    list_filter = ['title']
    inlines = [ApproxInline]


@admin_thumbnails.thumbnail('image')
class CityAdmin(admin.ModelAdmin):
    list_display = [ 'title','slug',]
    list_filter = ['state']
    inlines = [ApproxInline]
    readonly_fields = ('slug',)


@admin_thumbnails.thumbnail('image')
class LocalityAdmin(admin.ModelAdmin):
    list_display = [ 'title','slug',]
    list_filter = ['city']
    inlines = [ApproxInline]
    readonly_fields = ('slug',)


class ApproxAdmin(admin.ModelAdmin):
    list_display = [ 'category', 'city','locality','total']
    list_filter = ['category', 'city','locality',]

class StateAdmin(admin.ModelAdmin):
    list_display = [ 'country', 'state']
    list_filter = ['country',]

admin.site.register(Category,CategoryAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Find_From,)
admin.site.register(Call_Status,)
admin.site.register(Approx,)
admin.site.register(SocialSite,)
admin.site.register(KeyWords,)
admin.site.register(Country,)
admin.site.register(State,StateAdmin)
