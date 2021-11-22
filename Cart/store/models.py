from django.db import models
from django.urls import reverse
from cat.models import cat


class product(models.Model):
    product_name = models.CharField(max_length=500, unique=True)
    product_slug = models.SlugField(max_length=500, unique=True)
    product_desc = models.TextField(max_length=500, blank=True)
    product_price = models.IntegerField()
    product_img = models.ImageField(upload_to="img/product", blank=True)
    product_stock = models.IntegerField()
    product_is_available = models.BooleanField(default=True)
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_modified_date = models.DateTimeField(auto_now=True)
    product_cat = models.ForeignKey(cat, on_delete=models.CASCADE)
    # class meta:
    #     ordering =[id]
    def get_url(self):
        return reverse('product_details',args=[self.product_cat.cat_slug,self.product_slug])

    def __str__(self):
        return self.product_name
variation_category_choice = (
    ('color','color'),
    ('size','size')
)
class variation(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100,choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.product

# Create your models here.
