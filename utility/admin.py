from django.contrib import admin

# Register your models here.

from .models import *


class ApproxInline(admin.TabularInline):
    model = Approx
    extra = 1
    show_change_link = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'title','image_tag']
    list_filter = ['title']
    readonly_fields = ('image_tag',)
    inlines = [ApproxInline]

class ApproxAdmin(admin.ModelAdmin):
    list_display = [ 'category', 'city','locality','total']
    list_filter = ['category', 'city','locality',]

class StateAdmin(admin.ModelAdmin):
    list_display = [ 'country', 'state']
    list_filter = ['country',]

admin.site.register(Category,CategoryAdmin)
admin.site.register(City)
admin.site.register(Locality)
admin.site.register(Find_From,)
admin.site.register(Call_Status,)
admin.site.register(Approx,)
admin.site.register(SocialSite,)
admin.site.register(KeyWords,)
admin.site.register(Country,)
admin.site.register(State,StateAdmin)
