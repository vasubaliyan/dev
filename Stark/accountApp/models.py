from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="account")
    user_name=models.CharField(max_length=30,default=None,null=True)
    password=models.CharField(max_length=20,default=None,null=True)
    confirm_password=models.CharField(max_length=20,default=None,null=True)

