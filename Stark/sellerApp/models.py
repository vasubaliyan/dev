from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from utils.utils import StatusMixin


class Seller(StatusMixin):
    seller_name=models.CharField(max_length=20,null=True,default=None)
    seller_user_name=models.CharField(max_length=20,null=True,default=None)
    seller_password=models.CharField(max_length=20,null=True,default=None)
    seller_email=models.EmailField(max_length=30,null=True)
    seller_number=PhoneNumberField(null=True,blank=True)
    seller_address_line1=models.CharField(max_length=20,null=True,default=None)
    seller_address_line2=models.CharField(max_length=20,null=True,default=None)
    seller_image=models.ImageField(upload_to="seller/photos/%Y/%m/%d",null=True)
    seller_state=models.CharField(max_length=20,null=True,default=None)
    seller_district=models.CharField(max_length=20,null=True,default=None)
    seller_city=models.CharField(max_length=20,null=True,default=None)
    seller_pin_code=models.IntegerField(null=True)
    seller_status=models.BooleanField(default=True)
    seller_adharcard_front_image=models.ImageField(upload_to="adhar/photos/%Y/%m/%d",null=True)
    seller_adharcard_back_image=models.ImageField(upload_to="adhar/photos/%Y/%m/%d",null=True)


    def __str__(self):
        return self.seller_name


