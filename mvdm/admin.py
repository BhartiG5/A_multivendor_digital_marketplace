from itertools import product
from operator import index
from django.contrib import admin
from .models import OrderDetail, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(OrderDetail)
