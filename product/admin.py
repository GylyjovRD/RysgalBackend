from django.contrib import admin
from django.utils.html import format_html

from .models import (Settings, Banner, Category, SubCategory, Brand, Product,
        Images, Attribute, Comments, SampleImages, Cashback, Stores, Services,
        CompanySettings, Messages, UserAgreement, AboutUs, GifBanner, Medias,
        Background)

class ProductAttributeInline(admin.StackedInline):
        model = Attribute
        extra = 1

class ProductImageInline(admin.StackedInline):
        model = Images
        extra = 2

class ProductAdmin(admin.ModelAdmin):
        def image_tag(self, obj):
                return format_html('<img src="{0}" style="width: 45px; height:45px;">'.format(obj.main_image.url))
        list_display = ["image_tag", "title_tm", "price", "is_usd", "is_special", "is_active", "is_main"]
        list_editable = ["price", "is_usd", "is_special", "is_active", "is_main"]
        search_fields = ["title_tm", "title_ru", "title_en"]
        list_per_page = 40
        list_display_links = ("image_tag", "title_tm")
        inlines = [ProductImageInline, ProductAttributeInline]

class SettingsAdmin(admin.ModelAdmin):
        list_display = ['course', 'created_at']

class BannerAdmin(admin.ModelAdmin):
        def image_tag(self, obj):
                return format_html('<img src="{0}" style="width: 45px; height:45px;">'.format(obj.image.url))
        list_display = ['image_tag','title']

class SampleImagesAdmin(admin.ModelAdmin):
        def image_tag(self, obj):
                return format_html('<img src="{0}" style="width: 45px; height:45px;">'.format(obj.image.url))
        list_display = ['image_tag', 'title']

class CategorySubInline(admin.StackedInline):
        model = SubCategory
        extra = 1

class CategoryAdmin(admin.ModelAdmin):
        def image_tag(self, obj):
                return format_html('<img src="{0}" style="width: 45px; height:45px;">'.format(obj.image.url))
        list_display = ["image_tag", "title_tm"]
        inlines = [CategorySubInline]

class CommentsAdmin(admin.ModelAdmin):
        list_display = ["product", "user", "title", "is_active"]
        list_editable = ["is_active"]

admin.site.register(Settings, SettingsAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(SampleImages,SampleImagesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Cashback)
admin.site.register(Stores)
admin.site.register(Services)
admin.site.register(CompanySettings)
admin.site.register(Messages)
admin.site.register(UserAgreement)
admin.site.register(AboutUs)
admin.site.register(GifBanner)
admin.site.register(Medias)
admin.site.register(Background)