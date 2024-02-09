from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe
# Create your models here.
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.db.models.signals import pre_save
from utility.models import City, Locality

from django.utils.text import slugify


class Society_Building(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE) #many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE) #many to one relation with Brand
    name = models.CharField(max_length=150) 
    image=models.ImageField(blank=True,upload_to='images/')
    google_map = models.CharField(max_length=1000,unique=True,blank=True,) 
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='1. Society_Building'



    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name  + '' + self.locality.title + '' + self.city.title)
        super(Locality ,self).save(*args , **kwargs)
    
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('locality_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Images(models.Model):
    society=models.ForeignKey(Society_Building,on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.society
    
    class Meta:
        verbose_name_plural='2. Images'

