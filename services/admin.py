
from django.contrib import admin
from .models import(
    Technology,
    Industry, 
    Category, 
    AboutProduct, 
    ProductFAQ, 
    Product,
    Gallery, 
    ProductSlide,
    Enquiry,
    Configuration,
    ConfigurationKeyPoint,
)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'technology_type',
        'is_featured',
        'is_active',
        'display_order',
    )

    list_filter = (
        'technology_type',
        'is_featured',
        'is_active',
    )

    search_fields = (
        'name',
        'description',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    list_editable = (
        'is_featured',
        'is_active',
        'display_order',
    )

    ordering = ('display_order', 'name')

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'is_featured',
        'is_active',
        'display_order',
    )

    list_filter = (
        'is_featured',
        'is_active',
    )

    search_fields = (
        'name',
        'description',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    list_editable = (
        'is_featured',
        'is_active',
        'display_order',
    )

    ordering = ('display_order', 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'parent',
        'is_featured',
        'is_active',
        'display_order',
    )

    list_filter = (
        'parent',
        'is_featured',
        'is_active',
    )

    search_fields = (
        'name',
        'description',
    )

    autocomplete_fields = ('parent',)

    prepopulated_fields = {
        'slug': ('name',)
    }

    list_editable = (
        'is_featured',
        'is_active',
        'display_order',
    )

    ordering = ('display_order', 'name')


class AboutProductInline(admin.StackedInline):
    model = AboutProduct
    extra = 0

class ProductSlideInline(admin.StackedInline):
    model = ProductSlide
    extra = 0


class ProductFAQInline(admin.StackedInline):
    model = ProductFAQ
    extra = 0

class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'is_active',
        'created_at',
    )

    search_fields = ('name', 'slug')

    prepopulated_fields = {
        'slug': ('name',)
    }

    list_filter = ('is_active',)

    inlines = [
        AboutProductInline,
        ProductFAQInline,
        GalleryInline,
        ProductSlideInline,
    ]


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'email',
        'product',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'product',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'phone',
        'subject',
        'product__name',
    )

    list_editable = (
        'status',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Customer Information', {
            'fields': (
                'name',
                'email',
                'phone',
            )
        }),

        ('Enquiry Information', {
            'fields': (
                'product',
                'subject',
                'message',
                'status',
            )
        }),

        ('Admin Notes', {
            'fields': (
                'admin_notes',
            )
        }),

        ('Date Information', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )


class ConfigurationKeyPointInline(admin.TabularInline):

    model = ConfigurationKeyPoint
    extra = 1


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'product',
        'price',
        'is_active',
        'display_order',
    )

    list_filter = (
        'product',
        'is_active',
    )

    search_fields = (
        'name',
        'product__name',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    list_editable = (
        'is_active',
        'display_order',
    )

    inlines = [
        ConfigurationKeyPointInline,
    ]
