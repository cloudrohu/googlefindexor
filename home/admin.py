from django.contrib import admin
from .models import Settings , Slider
from django.utils.html import format_html

# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):

    list_display = (
        "site_name",
        "phone_number",
        "email",
    )

    search_fields = (
        "site_name",
        "email",
        "phone_number",
    )

    fieldsets = (

        (
            "🏠 Basic Information",
            {
                "fields": (
                    "site_name",
                    "logo",
                    "favicon",
                    "offer_banner",
                )
            }
        ),

        (
            "🔍 SEO & Meta Information",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "meta_keywords",
                    "meta_author",
                    "og_title",
                    "og_description",
                    "og_image",
                )
            }
        ),

        (
            "🎴 Card Design",
            {
                "fields": (
                    "front_view_card",
                    "back_view_card",
                    "alternate_design_card",
                )
            }
        ),

        (
            "📱 Social Media",
            {
                "fields": (
                    "facebook_url",
                    "twitter_url",
                    "instagram_url",
                    "youtube_url",
                    "linkedin_url",
                )
            }
        ),

        (
            "📞 Contact Information",
            {
                "fields": (
                    "phone_number",
                    "email",
                    "address",
                    "google_iframe",
                )
            }
        ),

        (
            "🦶 Footer Information",
            {
                "fields": (
                    "footer_text",
                    "copyright",
                )
            }
        ),
    )

    # Only one settings record
    def has_add_permission(self, request):
        return not Settings.objects.exists()
    


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    list_display = (
        "image_thumbnail",
        "title1",
        "title2",
        "descriptions",
        "badge_title",

    )

    def image_thumbnail(self, obj):
        if obj.image: # Assumes 'image' is the field name on your model
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 4px;" />', obj.image.url)
        return "No Image"

    # Set the column header name in the admin panel
    image_thumbnail.short_description = 'Thumbnail'