from django.contrib import admin
from .models import product,variation
class productAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_price','product_img','product_is_available','product_modified_date','product_stock','product_cat']
    prepopulated_fields = {'product_slug': ('product_name',)}

class variationAdmin(admin.ModelAdmin):
    list_display = ['product','variation_category','variation_value','is_active']
    list_editable = ('is_active','variation_value',)
    list_filter = ('product','variation_category','variation_value',)
admin.site.register(product,productAdmin)
admin.site.register(variation,variationAdmin)

# Register your models here.
# product_name = models.CharField(max_length=500, unique=True)
#     product_slug = models.SlugField(max_length=500, unique=True)
#     product_desc = models.TextField(max_length=500, blank=True)
#     product_price = models.ImageField()
#     product_img = models.ImageField(upload_to="img/product", blank=True)
#     product_stock = models.ImageField()
#     product_is_available = models.BooleanField(default=True)
#     product_created_date = models.DateTimeField(auto_now_add=True)
#     product_modified_date = models.DateTimeField(auto_now=True)
#     product_cat = models.ForeignKey(cat, on_delete=models.CASCADE)