from django.contrib import admin
from .models import product, variation, RatingReview


class productAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_price','product_img','product_is_available','product_modified_date','product_stock','product_cat']
    prepopulated_fields = {'product_slug': ('product_name',)}

class variationAdmin(admin.ModelAdmin):
    list_display = ['product','variation_category','variation_value','is_active']
    list_editable = ('is_active','variation_value',)
    list_filter = ('product','variation_category','variation_value',)
admin.site.register(product,productAdmin)
admin.site.register(variation,variationAdmin)
admin.site.register(RatingReview)

