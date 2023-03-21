from django.db import models
from utils.utils import StatusMixin
from brandApp.models import Brand
from categoryApp.models import Category
from subcategoryApp.models import Subcategory


class Product(StatusMixin):
    product_name=models.CharField(max_length=20,null=True,default=None)
    product_description=models.CharField(max_length=20,null=True,default=None)
    product_brand=models.ManyToManyField(Brand,related_name="product_brand")
    product_quantity=models.IntegerField()
    product_mrp=models.IntegerField()
    product_front_image=models.ImageField(upload_to='product/photos/%Y/%m/%d',null=True)
    product_back_image=models.ImageField(upload_to='product/photos/%Y/%m/%d',null=True)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product_category")
    product_subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="product_subcategory")


    def __str__(self):
        return self.product_name


