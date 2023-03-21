from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from utils.utils import StatusMixin

class Buyers(StatusMixin):
    buyer_name=models.CharField(max_length=20,null=True,default=None)
    buyers_user_name=models.CharField(max_length=20,null=True,default=None)
    buyers_password=models.CharField(max_length=20,null=True,default=None)
    buyers_email=models.EmailField(max_length=30,null=True)
    buyers_number=PhoneNumberField(null=True)
    buyers_counter=models.IntegerField()
    buyers_address_line1=models.CharField(max_length=20,null=True,default=None)
    buyers_address_line2=models.CharField(max_length=20,null=True,default=None)
    buyers_image=models.ImageField(upload_to="buyres/photos/%Y/%m/%d",null=True)
    buyers_state=models.CharField(max_length=20,null=True,default=None)
    buyers_district=models.CharField(max_length=20,null=True,default=None)
    buyers_city=models.CharField(max_length=20,null=True,default=None)
    buyers_pin_code=models.IntegerField(null=True)
    buyers_status=models.BooleanField(default=True)
    byures_adharcard_front_image=models.ImageField(upload_to="adhar/photos/%Y/%m/%d",null=True)
    buyers_adharcard_back_image=models.ImageField(upload_to="adhar/photos/%Y/%m/%d",null=True)


    def __str__(self):
        return self.buyer_name