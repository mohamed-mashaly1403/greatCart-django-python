

from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse
from cat.models import cat

from accounts.models import account


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
        return reverse('product_details', args=[self.product_cat.cat_slug, self.product_slug])
    def averagereview(self):
        reviews = RatingReview.objects.filter(product=self,status=True).aggregate(average=Avg('rating'))
        avg =0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
            return avg
    def countreview(self):
        reviews = RatingReview.objects.filter(product=self,status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
            return count



    def __str__(self):
        return self.product_name


class variationManager(models.Manager):
    def color(self):
        return super(variationManager, self).filter(variation_category='color', is_active=True)

    def size(self):
        return super(variationManager, self).filter(variation_category='size', is_active=True)


variation_category_choice = (
    ('color', 'color'),
    ('size', 'size')
)


class variation(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    objects = variationManager()

    def __str__(self):
        return self.variation_value


# Create your models here.
class RatingReview(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20,blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject
#product gallery for every product
class ProductGallery(models.Model):
    product = models.ForeignKey(product,default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/Gallery',max_length=255)
    def __str__(self):
        return self.product.product_name
    class Meta:
        verbose_name='ProductGallery'
        verbose_name_plural='Product Gallery'



