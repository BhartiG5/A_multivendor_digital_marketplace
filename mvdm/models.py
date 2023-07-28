from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

    def __str__(self):
        return self.name

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads')
    total_sales_amount = models.IntegerField(default=0)
    total_sales = models.IntegerField(default=0)


class OrderDetail(models.Model):

    def __str__(self):
        return self.customer_name

    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    has_paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


