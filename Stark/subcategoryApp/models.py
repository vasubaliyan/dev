from django.db import models
from utils.utils import StatusMixin

class Subcategory(StatusMixin):
    subcategory_name=models.CharField(max_length=10,null=True,default=None)
    subcategory_description=models.CharField(max_length=20,null=True,default=None)
