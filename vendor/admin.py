import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from .models import Company,Comment,Error,Faq,Follow_Up,Images,Meeting,SocialLink,Visit

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    show_change_link = True

class ErrorInline(admin.TabularInline):
    model = Error
    extra = 1
    show_change_link = True

class FaqInline(admin.TabularInline):
    model = Faq
    extra = 1
    show_change_link = True

class Follow_UpInline(admin.TabularInline):
    model = Follow_Up
    extra = 1
    show_change_link = True

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1
    show_change_link = True
class MeetingInline(admin.TabularInline):
    model = Meeting
    extra = 1
    show_change_link = True

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1
    show_change_link = True

class VisitInline(admin.TabularInline):
    model = Visit
    extra = 1
    show_change_link = True

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['image_tag','category','call_status', 'find_from', 'contact_person', 'contact_no', 'email','city','locality','address','keywords', 'website', 'create_at','update_at','updated_by']
    list_filter = ['category','category','call_status', 'find_from','city','locality',]
    readonly_fields = ('image_tag',)
    inlines = [CommentInline,ErrorInline,FaqInline,Follow_UpInline,ImagesInline,MeetingInline,MeetingInline,SocialLinkInline,VisitInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment', 'company','status','create_at','rate','ip']
    list_filter = ['status']
    list_editable = ['status']
    readonly_fields = ('subject','comment','ip','user','company','rate','id')

class ErrorAdmin(admin.ModelAdmin):
    list_display = ['company','title','error']

class FaqAdmin(admin.ModelAdmin):
    list_display = ['company','questions','answers', 'create_at', 'update_at']

class Follow_UpAdmin(admin.ModelAdmin):
    list_display = ['company','follow_up','comment', 'create_at', 'update_at']

class VisitAdmin(admin.ModelAdmin):
    list_display = ['company','visit_date','comment', 'create_at', 'update_at']

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['company','meeting','comment', 'create_at', 'update_at']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Error,ErrorAdmin)
admin.site.register(Faq,FaqAdmin)
admin.site.register(Follow_Up,Follow_UpAdmin)
admin.site.register(Images,)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(SocialLink,)
admin.site.register(Visit,VisitAdmin)