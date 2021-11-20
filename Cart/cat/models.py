from django.db import models
from django.urls import reverse

# Create your models here.
class cat(models.Model):
    cat_name = models.CharField(max_length=100,unique=True)
    cat_slug = models.SlugField(max_length=150,unique=True)
    cat_desc = models.TextField(max_length=500,blank=True)
    cat_img = models.ImageField(upload_to="img/cat",blank=True)
    class Meta:
        verbose_name='cat'
        verbose_name_plural='cat'
    def get_url(self):
        return reverse('products_by_cat',args=[self.cat_slug])

    def __str__(self):
        return self.cat_name

