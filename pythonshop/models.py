from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model): 
    user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50,null=False)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=False, blank=False)
    image = models.ImageField(null=False,blank=True)

    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null= True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=False, blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null= True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null= True)
    quantity = models.IntegerField(default = 0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.product.name)
    @property
    def get_total(self):
            total = self.quantity * self.product.price
            return total
class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null= True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null= True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=10,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.address
