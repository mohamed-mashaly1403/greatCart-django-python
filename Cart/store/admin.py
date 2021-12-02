from django.contrib import admin
from .models import product, variation, RatingReview, ProductGallery
import admin_thumbnails
@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1



class productAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_price','product_img','product_is_available','product_modified_date','product_stock','product_cat']
    prepopulated_fields = {'product_slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class variationAdmin(admin.ModelAdmin):
    list_display = ['product','variation_category','variation_value','is_active']
    list_editable = ('is_active','variation_value',)
    list_filter = ('product','variation_category','variation_value',)
admin.site.register(product,productAdmin)
admin.site.register(variation,variationAdmin)
admin.site.register(RatingReview)
admin.site.register(ProductGallery)

