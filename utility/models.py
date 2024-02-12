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

from django.utils.text import slugify


class Country(models.Model):
    country_name  = models.CharField(max_length=50)
    country_code  = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name
    
    class Meta:
        verbose_name_plural='9. Country'


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state  = models.CharField(max_length=50)

    def __str__(self):
        return self.state
    
    class Meta:
        verbose_name_plural='8. State'
    

class City(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    state = models.ForeignKey(State, on_delete=models.CASCADE,blank=True, null=True ,)
    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)
    featured_category = models.BooleanField(default=False)
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='7. City'
    
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title + '-' +self.state.state)
        super(City ,self).save(*args , **kwargs)
    
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug': self.slug})


class Locality(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)
    featured_category = models.BooleanField(default=False)
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + '-' +self.city.title
    
    class Meta:
        verbose_name_plural='10. Locality'
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title + '-' +self.city.title)
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



class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)
    featured_category = models.BooleanField(default=False)
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

   
    class Meta:
        verbose_name_plural='1. Category'
        
    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Category ,self).save(*args , **kwargs)
    
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Find_From(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='4. Find_From'
    
    
class SocialSite(models.Model):
    name = models.CharField(max_length=50)
    icon_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='5. SocialSite'
    

class Call_Status(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='6. Call_Status'
    

class Approx(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Brand
    city = models.ForeignKey(City, on_delete=models.CASCADE) #many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE) #many to one relation with Brand
    total = models.CharField(max_length=50,unique=True)    
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.total
    
    class Meta:
        verbose_name_plural='3. Approx'

    