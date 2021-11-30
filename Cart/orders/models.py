from django.db import models
from accounts.models import account
from store.models import product,variation



class Payment(models.Model):
    user = models.ForeignKey(account,on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.payment_id



class Order(models.Model):
    status = (
        ('new','new'),
        ('accepted','accepted'),
        ('completed','completed'),
        ('canceled','canceled')
    )
    user = models.ForeignKey(account, on_delete=models.SET_NULL,null=True)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50,blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_note = models.CharField(max_length=100,blank=True)
    total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=10,choices=status,default='new')
    ip= models.CharField(max_length=20,blank=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self. first_name


class orderPoduct(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    user = models.ForeignKey(account, on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    variations = models.ManyToManyField(variation,blank=True)
    color =models.CharField(max_length=50,blank=True)
    size =models.CharField(max_length=50,blank=True)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.product











