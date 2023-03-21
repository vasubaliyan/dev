from django.db import models
from utils.utils import StatusMixin


class Brand(models.Model):
    brand_name=models.CharField(max_length=20,null=True,default=None)


    def __str__(self):
        return self.brand_name
