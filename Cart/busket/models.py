from django.db import models
from store.models import product,variation

from accounts.models import account


class buskett(models.Model):
	objects = models.Manager()

	cart_id = models.CharField(max_length=205,blank=True)
	cart_date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.cart_id
class busketItems(models.Model):
	objects = models.Manager()
	user = models.ForeignKey(account,on_delete=models.CASCADE,null=True)
	product_busket_item = models.ForeignKey(product,on_delete=models.CASCADE)
	variations = models.ManyToManyField(variation,blank=True)
	busket_item = models.ForeignKey(buskett,on_delete=models.CASCADE,null=True)
	quantity = models.IntegerField()
	busketItems_is_active = models.BooleanField(default=True)
	def sub_total(self):
		return self.product_busket_item.product_price * self.quantity
	def __unicode__(self):
		return self.product_busket_item


# Create your models here.
