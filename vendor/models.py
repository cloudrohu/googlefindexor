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
from utility.models import Find_From,Category,City,Locality,SocialSite
from home.models import Society_Building


from django.utils.text import slugify


class Company(models.Model):

    Call_Status = (
        ('New', 'New'),
        ('Foloow_Up', 'Foloow_Up'),
        ('Meeting', 'Meeting'),
        ('Deal_Done', 'Deal_Done'),
        ('Call Not Receive', 'Call Not Receive'),
        ('Not Interested', 'Not Interested'),
        ('Deal_Done', 'Deal_Done'),
        ('Call Cut', 'Call Cut'),
    )
           
    company_name = models.CharField(max_length=250,unique=True)
    contact_person = models.CharField(max_length=255,null=True , blank=True)
    contact_no = models.CharField(max_length=255,null=True , blank=True)
    whatsapp_no = models.CharField(max_length=255,null=True , blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE) #many to one relation with Brand     
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE) #many to one relation with Brand 
    society_building = models.ForeignKey(Society_Building, on_delete=models.CASCADE,null=True , blank=True) #many to one relation with Brand    
    find_from = models.ForeignKey(Find_From, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand
    email_id = models.EmailField(null=True,blank=True)
    website = models.CharField(max_length=255,null=True , blank=True)
    address = models.CharField(max_length=255,null=True , blank=True)
    google_map = models.CharField(max_length=1000,null=True , blank=True)
    description = models.TextField(max_length=5000,null=True , blank=True)
    image=models.ImageField(upload_to='images/')
    call_status=models.CharField(max_length=50,choices=Call_Status, default='New')
    call_comment = models.TextField(max_length=5000,null=True , blank=True)
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, related_name='created_by_user',on_delete=models.CASCADE,null=True,blank=True,)
    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name_plural='1. Company'


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def save(self , *args , **kwargs):
        self.slug = slugify(self.company_name + '-' + self.locality.title + '-' + self.city.title)
        super(Company ,self).save(*args , **kwargs)


    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})  
    
    
    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

class Social(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE) #many to one relation with Brand       
    facebook = models.CharField(max_length=255,null=True , blank=True)
    twitter = models.CharField(max_length=255,null=True , blank=True)
    instagram = models.CharField(max_length=255,null=True , blank=True)
    pinterest = models.CharField(max_length=255,null=True , blank=True)
    youtube = models.CharField(max_length=255,null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.facebook
    
    class Meta:
        verbose_name_plural='6. Social'


class Images(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='9. Images'

class User_Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name_plural='4. User_Comment'

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    comment = models.CharField(max_length=250,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name_plural='13. Comment'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

    class Meta:
        verbose_name_plural='7. Approx'


class SocialLink(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand
    socia_site = models.ForeignKey(SocialSite, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand
    link = models.CharField(max_length=50,unique=True)    
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link
    
    class Meta:
        verbose_name_plural='7. SocialLink'
    
class Error(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand
    title = models.CharField(max_length=500,unique=True)    
    error = models.CharField(max_length=500,unique=True)    
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='3. Error'

class Follow_Up(models.Model):
    company = models.ForeignKey(Company,blank=True, null=True , on_delete=models.CASCADE)
    follow_up = models.DateTimeField(blank=True, null=True,)
    comment = models.CharField(max_length=500,blank=True, null=True,)

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment 
        
    class Meta:
        verbose_name_plural='10. Follow_Up'


class Faq(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    questions = models.CharField(max_length=500,blank=True)
    answers = models.TextField(blank=True,)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.questions
    
    class Meta:
        verbose_name_plural='8. Faq'

class Meeting(models.Model):
    company = models.ForeignKey(Company,blank=True, null=True , on_delete=models.CASCADE)
    meeting = models.DateTimeField(null=True, blank=True)
    comment = models.CharField(max_length=500,blank=True, null=True,)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment 
    
    class Meta:
        verbose_name_plural='11. Meeting'
    
class Visit(models.Model):
    company = models.ForeignKey(Company,blank=True, null=True , on_delete=models.CASCADE)
    comment = models.CharField(max_length=500,blank=True, null=True,)
    visit_date=models.DateTimeField(auto_now_add=True,)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment 
    
    class Meta:
        verbose_name_plural='12. Visit'  
