import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from .models import Company,User_Comment,Error,Faq,Follow_Up,Images,Meeting,SocialLink,Visit,Company_Info,DealIn,Comment,Social


class DealInInline(admin.TabularInline):
    model = DealIn
    extra = 1
    show_change_link = True

class SocialInline(admin.TabularInline):
    model = Social
    extra = 1
    show_change_link = True


class Company_InfoInline(admin.TabularInline):
    model = Company_Info
    extra = 1
    show_change_link = True


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
    list_display = ['company_name','contact_no', 'city', 'locality', 'slug','create_at','update_at',]
    list_filter = ['city','locality','create_at','update_at',]
    search_fields = ['company_name','contact_no',]
    readonly_fields = ('created_by','slug')
    list_per_page = 25
    inlines = [Company_InfoInline,CommentInline,SocialInline,ErrorInline,Follow_UpInline,MeetingInline,SocialLinkInline,VisitInline,DealInInline,FaqInline,ImagesInline]
   


class Company_InfoAdmin(admin.ModelAdmin):
    list_display = ['image_tag','category','call_status', 'find_from', 'contact_person', 'contact_no', 'email_id','address','website', 'create_at','update_at','updated_by']
    list_filter = ['category','call_status', 'find_from',]
    readonly_fields = ('create_at',)
    list_per_page = 25


class User_CommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment', 'company','status','create_at','rate','ip']
    list_filter = ['status']
    list_editable = ['status']
    readonly_fields = ('subject','comment','ip','user','company','rate','id')
    list_per_page = 25


class ErrorAdmin(admin.ModelAdmin):
    list_display = ['company','title','error']
    list_per_page = 25


class FaqAdmin(admin.ModelAdmin):
    list_display = ['company','questions','answers', 'create_at', 'update_at']
    list_per_page = 25


class Follow_UpAdmin(admin.ModelAdmin):
    list_display = ['company','follow_up','comment', 'create_at', 'update_at']
    list_per_page = 25


class VisitAdmin(admin.ModelAdmin):
    list_display = ['company','visit_date','comment', 'create_at', 'update_at']
    list_per_page = 25


class MeetingAdmin(admin.ModelAdmin):
    list_display = ['company','meeting','comment', 'create_at', 'update_at']
    list_per_page = 25


admin.site.register(Company,CompanyAdmin)
admin.site.register(Company_Info,Company_InfoAdmin)

admin.site.register(Comment,)
admin.site.register(User_Comment,User_CommentAdmin)
admin.site.register(Error,ErrorAdmin)
admin.site.register(Faq,FaqAdmin)
admin.site.register(Follow_Up,Follow_UpAdmin)
admin.site.register(Images,)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(SocialLink,)
admin.site.register(Visit,VisitAdmin)
admin.site.register(DealIn)
admin.site.register(Social)