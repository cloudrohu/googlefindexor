from django.db import models

# Create your models here.

class Settings(models.Model):

    # BASIC INFO
    site_name = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    favicon = models.ImageField(upload_to='favicon/', blank=True, null=True)
    offer_banner = models.ImageField(upload_to='offer_banner/', blank=True, null=True)

    # META INFO
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    meta_author = models.CharField(max_length=100, blank=True, null=True)
    og_title = models.CharField(max_length=100, blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    og_image = models.ImageField(upload_to='og_images/', blank=True, null=True)

    # CARD INFO
    front_view_card = models.ImageField(upload_to='front_view_card/',blank=True,null=True)
    back_view_card = models.ImageField(upload_to='back_view_card/',blank=True,null=True)
    alternate_design_card = models.ImageField(upload_to='alternate_design_card/',blank=True,null=True)

    # SOCIAL MEDIA
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    # CONTACT INFO
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    google_iframe = models.TextField(blank=True, null=True)

    # FOOTER INFO
    footer_text = models.TextField(blank=True, null=True)
    copyright = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.site_name or "Site Settings"



class Slider(models.Model):

    image = models.ImageField(upload_to="hero/", blank=True, null=True)
    title1 = models.CharField(max_length=200, blank=True, null=True)
    title2 = models.CharField(max_length=300, blank=True, null=True)
    descriptions = models.CharField(max_length=1000, blank=True, null=True)
    badge_title = models.CharField(max_length=300, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Slider"
        verbose_name_plural = "1. Sliders"

    def __str__(self):
        return self.title1 or ""        