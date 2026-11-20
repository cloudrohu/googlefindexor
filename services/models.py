from django.db import models
from django.utils.text import slugify

# Create your models here.

class Technology(models.Model):

    TECHNOLOGY_TYPES = [
        ('language', 'Programming Language'),
        ('framework', 'Framework & Library'),
        ('cloud', 'Cloud & Hosting'),
        ('database', 'Database'),
        ('devops', 'DevOps & Infrastructure'),
        ('ai', 'AI & Automation'),
        ('api', 'API & Integration'),
        ('design', 'Design & Development Tools'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=150,unique=True)

    slug = models.SlugField(max_length=180,unique=True,blank=True)

    technology_type = models.CharField(max_length=30,choices=TECHNOLOGY_TYPES,default='other')

    short_description = models.CharField(max_length=250,blank=True)

    description = models.TextField(blank=True)

    logo = models.ImageField(upload_to='technologies/logos/',blank=True,null=True)

    website_url = models.URLField(blank=True)

    is_featured = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        ordering = ['display_order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Industry(models.Model):

    name = models.CharField(max_length=150,unique=True)

    slug = models.SlugField(max_length=180,unique=True,blank=True)

    short_description = models.CharField(max_length=250,blank=True)

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='industries/',blank=True,null=True)

    icon = models.CharField(max_length=100,blank=True,help_text="Font Awesome icon class")

    website_url = models.URLField(blank=True)

    is_featured = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Industry"
        verbose_name_plural = "Industries"
        ordering = ['display_order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=150,unique=True)

    slug = models.SlugField(max_length=180,unique=True,blank=True)

    parent = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,related_name='subcategories')

    short_description = models.CharField(max_length=250,blank=True)

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='categories/',blank=True,null=True)

    icon = models.CharField(max_length=100,blank=True,help_text="Font Awesome icon class")

    is_featured = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['display_order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} → {self.name}"

        return self.name


class Product(models.Model):

    name = models.CharField(max_length=200)

    slug = models.SlugField(unique=True,blank=True)

    short_description = models.CharField(max_length=300,blank=True)

    description = models.TextField(blank=True)

    logo = models.ImageField(upload_to='products/',blank=True,null=True)

    image = models.ImageField(upload_to='products/',blank=True,null=True)

    website_url = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AboutProduct(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='about_sections')

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(upload_to='products/about/',blank=True,null=True)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.product.name} - {self.title}"


class ProductSlide(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='slides')

    title = models.CharField(max_length=200)

    subtitle = models.CharField(max_length=250,blank=True)

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='products/slides/')

    button_text = models.CharField(max_length=100,blank=True)

    button_url = models.CharField(max_length=500,blank=True)

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = 'Product Slide'
        verbose_name_plural = 'Product Slides'

    def __str__(self):
        return f"{self.product.name} - {self.title}"


class ProductFAQ(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='faqs')

    question = models.CharField(max_length=300)

    answer = models.TextField()

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.question


class Gallery(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='gallery',blank=True)

    title = models.CharField(max_length=200,blank=True)

    image = models.ImageField(upload_to='products/gallery/')

    description = models.CharField(max_length=300,blank=True)

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return f"{self.product.name} - {self.title or 'Gallery Image'}"

class Enquiry(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('in_progress', 'In Progress'),
        ('qualified', 'Qualified'),
        ('closed', 'Closed'),
    ]

    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True,related_name='enquiries')

    name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    subject = models.CharField(max_length=200,blank=True)

    message = models.TextField()

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='new')

    admin_notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"{self.name} - {self.product or 'General Enquiry'}"


class Configuration(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='configurations',blank=True,null=True)

    name = models.CharField(max_length=200)

    slug = models.SlugField(unique=True,blank=True)

    short_description = models.CharField(max_length=300,blank=True)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

    image = models.ImageField(upload_to='products/configurations/',blank=True,null=True)

    is_active = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.name}"


class ConfigurationKeyPoint(models.Model):

    configuration = models.ForeignKey(
        Configuration,
        on_delete=models.CASCADE,
        related_name='key_points'
    )

    title = models.CharField(max_length=200)

    description = models.CharField(
        max_length=300,
        blank=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Font Awesome icon class"
    )

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = 'Configuration Key Point'
        verbose_name_plural = 'Configuration Key Points'

    def __str__(self):
        return self.title
